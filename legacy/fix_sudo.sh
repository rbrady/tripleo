#!/bin/bash

set -eux
TARGET_USER=$1
USER_FILE="/etc/sudoers.d/$1"

if [ -f $USER_FILE ]; then
    rm -rf $USER_FILE
fi

sudo echo "$1 ALL=(root) NOPASSWD:ALL" >> $USER_FILE
sudo chmod 0440 $USER_FILE

echo "passwordless sudo complete"

