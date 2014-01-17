#!/bin/bash

set -eux

$TRIPLEO_ROOT/diskimage-builder/bin/disk-image-create $NODE_DIST \
    -a amd64 \
    -o $TRIPLEO_ROOT/overcloud-control \
    boot-stack cinder cinder-api cinder-volume os-collect-config neutron-network-node \
    dhcp-all-interfaces swift-proxy swift-storage \

$TRIPLEO_ROOT/diskimage-builder/bin/disk-image-create \
	-a amd64 \
	--min-tmpfs -u \
	--offline \
	-o $TRIPLEO_ROOT/overcloud-cinder-volume \
	fedora selinux-permissive cinder cinder-volume \
	neutron-openvswitch-agent heat-cfntools stackuser pip-cache

$TRIPLEO_ROOT/diskimage-builder/bin/disk-image-create \
	-a amd64 \
	--min-tmpfs -u \
	--offline \
	-o $TRIPLEO_ROOT/overcloud-cinder-volume-n \
	fedora selinux-permissive cinder cinder-volume \
	heat-cfntools stackuser pip-cache
