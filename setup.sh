#! /bin/bash

set -eux

# install prereqs

# get extras

# fix sudo

# set selinux to permissive
sudo sed -i "s/=enforcing/=permissive/"

# clone undercloud-live

echo "The machine has been prepared to become the undercloud.  You must reboot to complete the selinux configuration changes."
