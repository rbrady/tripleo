#! /bin/bash

set -eux

# install prereqs
sudo yum install -y git vim

# get extras
mkdir -p ~/extra
cd ~/extra
git clone https://github.com/rbrady/tripleo-heat-templates.git
git clone https://github.com/rbrady/flaming-octo-tyrion.git

# fix sudo
sudo flaming-octo-tyrion/fix_sudo.sh rh

# set selinux to permissive
sudo sed -i "s/=enforcing/=permissive/"

# clone undercloud-live
cd
git clone https://github.com/rbrady/undercloud-live

echo "The machine has been prepared to become the undercloud.  You must reboot to complete the selinux configuration changes."
