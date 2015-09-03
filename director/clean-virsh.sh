#!/bin/bash

set -eux
set -o pipefail

function vm_delete(){
    sudo virsh undefine $1 || true
    sudo virsh destroy $1 || true
}

# delete instack vm and remove its files
vm_delete instack
sudo rm -rf /var/lib/libvirt/images/instack.qcow2
sudo rm -rf /home/stack/instack.qcow2

# delete all of the baremetal vms
for vm in $(virsh list --all | awk '{print $2}'); do
    vm_delete $vm
done

