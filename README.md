# Cloud Validation adapter for OSTF

## Overview

Existing [OSTF](http://docs.mirantis.com/fuel-dev/develop/ostf_contributors_guide.html)
code provides a number of tests which cover a number of cases needed for cloud
validation. The downside of existing OSTF is that it is tightly coupled with
FUEL's nailgun. Given project aims to create standalone adapter for OSTF which
is independent of FUEL thus making it possible to run OSTF tests on any random
cloud (in theory).

## High-level design

 CLI tool that works with health check plugins
 Supported plugins:
  - fuel health check


## Usage


  $ cloudvalidation cloud-health-check {argument} [argument_parameters]

  Examples:

  $ cloudvalidation cloud-health-check list_plugins

+----------+------------------------------------------------------------------+
| Property | Value                                                            |
+----------+------------------------------------------------------------------+
| name     | fuel_health                                                      |
| suites   | fuel_health.tests.sanity.test_sanity_identity.SanityIdentityTest |
|          | fuel_health.tests.sanity.test_sanity_compute.SanityComputeTest   |
|          | fuel_health.tests.sanity.test_sanity_heat.SanityHeatTest         |
|          | fuel_health.tests.smoke.test_create_flavor.FlavorsAdminTest      |
+----------+------------------------------------------------------------------+

  $ cloudvalidation cloud-health-check list_plugin_suites --validation-plugin fuel_health

+----------+------------------------------------------------------------------+
| Property | Value                                                            |
+----------+------------------------------------------------------------------+
| suites   | fuel_health.tests.sanity.test_sanity_identity.SanityIdentityTest |
|          | fuel_health.tests.sanity.test_sanity_compute.SanityComputeTest   |
|          | fuel_health.tests.sanity.test_sanity_heat.SanityHeatTest         |
|          | fuel_health.tests.smoke.test_create_flavor.FlavorsAdminTest      |
+----------+------------------------------------------------------------------+

  $ cloudvalidation cloud-health-check list_plugin_tests --validation-plugin fuel_health

+----------+--------------------------------------------------------------------------------------+
| Property | Value                                                                                |
+----------+--------------------------------------------------------------------------------------+
| tests    | fuel_health.tests.sanity.test_sanity_identity.SanityIdentityTest:test_list_services  |
|          | fuel_health.tests.sanity.test_sanity_identity.SanityIdentityTest:test_list_users     |
|          | fuel_health.tests.sanity.test_sanity_compute.SanityComputeTest:test_list_flavors     |
|          | fuel_health.tests.sanity.test_sanity_compute.SanityComputeTest:test_list_images      |
|          | fuel_health.tests.sanity.test_sanity_compute.SanityComputeTest:test_list_instances   |
|          | fuel_health.tests.sanity.test_sanity_compute.SanityComputeTest:test_list_rate_limits |
|          | fuel_health.tests.sanity.test_sanity_compute.SanityComputeTest:test_list_snapshots   |
|          | fuel_health.tests.sanity.test_sanity_compute.SanityComputeTest:test_list_volumes     |
|          | fuel_health.tests.sanity.test_sanity_heat.SanityHeatTest:test_list_stacks            |
|          | fuel_health.tests.smoke.test_create_flavor.FlavorsAdminTest:test_create_flavor       |
+----------+--------------------------------------------------------------------------------------+
## Links

 * [OSTF contributor's guide](http://docs.mirantis.com/fuel-dev/develop/ostf_contributors_guide.html)
 * [OSTF source code](https://github.com/stackforge/fuel-ostf)
