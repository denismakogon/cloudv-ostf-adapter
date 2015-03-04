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

from oslo_utils import importutils

from cloudv_ostf_adapter.common import cfg

CONF = cfg.CONF

FUEL_HEALTH_CONF = importutils.import_module("fuel_health.config")


@FUEL_HEALTH_CONF.process_singleton
class MonkeyPatchFuelHealthConf(object):

    def __init__(self):
        self.register_opts()
        self.compute = cfg.CONF.compute
        self.identity = cfg.CONF.identity
        self.network = cfg.CONF.network
        self.volume = cfg.CONF.volume
        self.murano = cfg.CONF.murano
        self.heat = cfg.CONF.heat
        self.sahara = cfg.CONF.sahara

    def register_opts(self):
        FUEL_HEALTH_CONF.register_compute_opts(CONF)
        FUEL_HEALTH_CONF.register_identity_opts(CONF)
        FUEL_HEALTH_CONF.register_network_opts(CONF)
        FUEL_HEALTH_CONF.register_volume_opts(CONF)
        FUEL_HEALTH_CONF.register_murano_opts(CONF)
        FUEL_HEALTH_CONF.register_heat_opts(CONF)
        FUEL_HEALTH_CONF.register_sahara_opts(CONF)


FUEL_HEALTH_CONF.FileConfig = MonkeyPatchFuelHealthConf
