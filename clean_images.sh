#!/bin/bash

set -eux

IMAGES_DIR=/opt/stack/images

for ID in $(glance image-list | grep "\(bm-deploy\|overcloud-compute\|overcloud-control\)" | awk '{print $2}'); do
	glance image-delete $ID
done

rm -rf $IMAGES_DIR/overcloud-control.qcow2*
#rm -rf $IMAGES_DIR/overcloud-compute.qcow2*

echo "Done cleaning images"
