#!/bin/bash

set -eux

cp /opt/stack/tripleo-incubator/scripts/setup-endpoints.orig /opt/stack/tripleo-incubator/scripts/setup-endpoints
cp /opt/stack/tripleo-incubator/scripts/register-endpoint.orig /opt/stack/tripleo-incubator/scripts/register-endpoint
