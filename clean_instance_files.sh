#!/bin/bash

set -eux

for INSTANCE in $(ls /var/lib/nova/instances | grep "instance" | awk '{print $1}'); do
	rm -rf /var/lib/nova/instances/$INSTANCE
done


echo "Done cleaning instance files"
