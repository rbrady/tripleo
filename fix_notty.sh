#!/bin/bash

set -eux
TARGET_USER=$1
USER_FILE="/etc/sudoers.d/$1-notty"

if [ -f $USER_FILE ]; then
    rm -rf $USER_FILE
fi

sudo echo "Defaults:$1 !requiretty" >> $USER_FILE
sudo chmod 0440 $USER_FILE
sudo visudo -c

echo "notty complete"

