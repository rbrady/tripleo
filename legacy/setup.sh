#! /bin/bash

set -eux

# install prereqs
sudo yum install -y git vim

# clone undercloud-live
git clone https://github.com/rbrady/undercloud-live

# get extras
mkdir -p ~/extra
pushd ~/extra
git clone https://github.com/rbrady/tripleo-heat-templates.git
git clone https://github.com/rbrady/flaming-octo-tyrion.git

# fix sudo
pushd flaming-octo-tyrion
sudo ./fix_sudo.sh rh

# set selinux to permissive
sudo sed -i "s/=enforcing/=permissive/"

echo "The machine has been prepared to become the undercloud.  You must reboot to complete the selinux configuration changes."
