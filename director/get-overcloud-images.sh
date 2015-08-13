#!/bin/bash

set -eux
set -o pipefail

curl -L -O http://rhos-release.virt.bos.redhat.com/mburns/latest-images/overcloud-full.tar
curl -L -O http://rhos-release.virt.bos.redhat.com/mburns/latest-images/discovery-ramdisk.tar
curl -L -O http://rhos-release.virt.bos.redhat.com/mburns/latest-images/deploy-ramdisk-ironic.tar

tar -xvf overcloud-full.tar
tar -xvf discovery-ramdisk.tar
tar -xvf deploy-ramdisk-ironic.tar
