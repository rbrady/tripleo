#!/bin/bash

if [ "root" == $(whoami) ]; then
  echo "cannot run script as root.  use the stack user."
  exit 1
fi

sudo rpm -ivh http://rhos-release.virt.bos.redhat.com/repos/rhos-release/rhos-release-latest.noarch.rpm
sudo rhos-release 7-director
sudo yum install -y python-rdomanager-oscplugin
openstack undercloud install
