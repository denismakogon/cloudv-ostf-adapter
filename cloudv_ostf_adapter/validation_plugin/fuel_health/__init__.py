#    Copyright 2015 Mirantis, Inc
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import os
import sys

from nose import core
from oslo_utils import importutils

from cloudv_ostf_adapter.common import cfg
from cloudv_ostf_adapter.validation_plugin import base
from cloudv_ostf_adapter.validation_plugin.fuel_health import fuel_health_opts
from cloudv_ostf_adapter.validation_plugin.fuel_health import sanity
from cloudv_ostf_adapter.validation_plugin.fuel_health import smoke
from cloudv_ostf_adapter.validation_plugin.fuel_health import high_availability
from cloudv_ostf_adapter.validation_plugin.fuel_health import platform


CONF = cfg.CONF

SUITES = [
    sanity,
    smoke,
    high_availability,
    platform,
]


class FuelHealthPlugin(base.ValidationPlugin):

    test_executor = "%(test_module_path)s:%(class)s.%(test)s"
    fuel_health_opts.MonkeyPatchFuelHealthConf()

    def __init__(self, load_tests=True):
        super(FuelHealthPlugin, self).__init__(
            'fuel_health', SUITES, load_tests=load_tests)

    def _get_tests(self):
        try:
            return super(FuelHealthPlugin, self)._get_tests()
        except Exception:
            print("fuel_health is not installed.")

    def _collect_test(self, tests):
        test_suites_paths = []
        for test in tests:
            classpath, test_method = test.split(":")
            classname = classpath.split(".")[-1]
            module = importutils.import_class(
                classpath).__module__
            test_module_path = os.path.abspath(
                sys.modules[module].__file__)
            if test_module_path.endswith("pyc"):
                test_module_path = test_module_path[:-1]
            test_suites_paths.append(
                self.test_executor %
                {
                    'test_module_path': test_module_path,
                    'class': classname,
                    'test': test_method
                })
        return test_suites_paths

    def run_suites(self):
        test_suites_paths = self._collect_test(self.tests)
        test_suites_paths.append(CONF.nose_verbosity)
        os.environ.update(
            {"CUSTOM_FUEL_CONFIG": CONF.health_check_config_path})
        CONF.reload_config_files()
        print(core.TestProgram(
            argv=test_suites_paths).success)

    def _get_tests_by_suite(self, suite):
        tests = []
        for test in self.tests:
            if suite in test:
                tests.append(test)
        return tests

    def setup_execution(self, tests):
        test_suites_paths = self._collect_test(tests)
        test_suites_paths.append(CONF.nose_verbosity)
        os.environ.update(
            {"CUSTOM_FUEL_CONFIG": CONF.health_check_config_path})
        CONF.reload_config_files()
        return test_suites_paths

    def run_suite(self, suite):
        if ":" in suite:
            raise Exception(
                "%s is a test case, but not test suite." % suite)
        else:
            tests = self._get_tests_by_suite(suite)
            print("Running test suite: %s ..." % suite)
            print(core.TestProgram(
                argv=self.setup_execution(tests)).success)
