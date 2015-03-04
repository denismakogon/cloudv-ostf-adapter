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

from cloudv_ostf_adapter.common import utils
from cloudv_ostf_adapter.nose_plugin import discovery


class SuiteDescriptor(object):

    suite_attrs = ['test_group', 'tests']
    test_attrs = ['tests']

    def __init__(self, test_group_definition, tests):
        """
        Describes test specific test group
        @param test_group_definition: Test group definition
                                      (i.e. sanity, smoke, HA, platform)
        @type test_group_definition: basestring
        @param tests: list of tests per test group
        @type tests: list
        """
        self.test_group = test_group_definition
        self.tests = tests

    def print_tests_description(self):
        utils.print_list(self, self.test_attrs)

    def print_description(self):
        utils.print_dict(self)


class ValidationPlugin(object):

    def __init__(self, name, suites, load_tests=True):
        __suites = []
        for suite in suites:
            __suites.extend(suite.TESTS)

        self.name = name
        self.suites = __suites
        self._suites = suites
        self.tests = (self._get_tests()
                      if load_tests else [])

    def _get_tests(self):
        """
        Test collector
        """
        tests = []
        for suite in self._suites:
            _tests = discovery.do_test_discovery(
                suite.TESTS)
            tests.extend(_tests)
        return tests

    def descriptor(self):
        """
        Returns Plugin descriptor that contains:
         - plugin name
         - plugin suites
         - plugin tests
        """
        return {
            "name": self.name,
            "suites": self.suites,
            "tests": self.tests,
        }

    def run_suites(self):
        raise Exception("Plugin doesn't support suite execution.")