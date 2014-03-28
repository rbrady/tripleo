#!/bin/bash

set -eux

#sudo -i /opt/stack/tripleo-incubator/scripts/create-nodes 1 2048 20 amd64 1
export MACS=$(/opt/stack/tripleo-incubator/scripts/get-vm-mac baremetal_2)
TRIPLEO_ROOT=/opt/stack/images /opt/stack/tripleo-incubator/scripts/setup-baremetal 1 2048 20 amd64 "$MACS" undercloud-live
