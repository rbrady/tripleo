#!/bin/bash

set -eux

for ID in $(nova baremetal-node-list | grep "\(undercloud-live\)" | awk '{print $2}'); do
	nova baremetal-node-delete $ID
done

echo "Done cleaning images"
