#!/usr/bin/bash
set -eux
set -o pipefail

sudo rm -Rf /usr/lib/python2.7/site-packages/tripleo_common*
sudo python setup.py install
sudo systemctl restart openstack-mistral-executor
sudo systemctl restart openstack-mistral-engine
# this loads the actions via entrypoints
sudo mistral-db-manage populate
# make sure the new actions got loaded
mistral action-list | grep tripleo
