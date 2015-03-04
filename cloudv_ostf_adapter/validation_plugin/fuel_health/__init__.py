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

from cloudv_ostf_adapter.common import cfg
from cloudv_ostf_adapter.validation_plugin import base
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

    def __init__(self, load_tests=True):
        super(FuelHealthPlugin, self).__init__(
            'fuel_health', SUITES, load_tests=load_tests)
