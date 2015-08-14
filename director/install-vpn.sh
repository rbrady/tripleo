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

# if the archive isn't available, attempt to download it
if [ -n "$OPENVPN_ARCHIVE" ]; then
  curl -L -O $OPENVPN_ARCHIVE
fi

# configure openvpn
if [ -f 'openvpn.tar.gz' ]; then
  echo "openvpn file exists"
  tar -xvf openvpn.tar.gz
  sudo cp etc/openvpn/* /etc/openvpn/
  # fix jacked up archive
  curl -L -O https://raw.githubusercontent.com/rbrady/tripleo/master/director/phx2-udp.conf
  sudo mv phx2-udp.conf /etc/openvpn/
else
  echo "No openvpn.tar.gz file."
  echo "You need to manually configure openvpn"
fi
