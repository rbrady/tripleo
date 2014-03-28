#!/bin/bash
set -eux

$TRIPLEO_ROOT/diskimage-builder/bin/disk-image-create $NODE_DIST \
    -a $NODE_ARCH -o ./undercloud \
    boot-stack nova-baremetal os-collect-config dhcp-all-interfaces \
    ceilometer ceilometer-agent-central ceilometer-agent-compute \
    ceilometer-agent-notification ceilometer-api ceilometer-collector \
    neutron-dhcp-agent $DIB_COMMON_ELEMENTS ${UNDERCLOUD_DIB_EXTRA_ARGS:-} 2>&1 | \
    tee $TRIPLEO_ROOT/dib-undercloud.log
