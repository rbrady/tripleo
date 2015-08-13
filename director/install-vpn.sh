#!/bin/bash

set -eux
set -o pipefail

OPENVPN_ARCHIVE=${OPENVPN_ARCHIVE:-}

# enable passwordless sudo for the stack user
echo "stack ALL=(root) NOPASSWD:ALL" | sudo tee -a /etc/sudoers.d/stack
sudo chmod 0440 /etc/sudoers.d/stack

# install openvpn
sudo rpm -Uvh http://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-release-7-5.noarch.rpm
sudo yum install openvpn
sudo yum remove epel-release

# configure openvpn
if [ -n "$OPENVPN_ARCHIVE" ]; then
  curl -L -O $OPENVPN_ARCHIVE
  tar -xvf `basename $OPENVPN_ARCHIVE`
  sudo cp etc/openvpn/* /etc/openvpn/
else
  echo "OPENVPN_ARCHIVE not set.  Exiting."
fi
