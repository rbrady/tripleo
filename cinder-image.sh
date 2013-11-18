$TRIPLEO_ROOT/diskimage-builder/bin/disk-image-create \
	-a amd64 \
	--min-tmpfs 3 -u \
	--offline \
	-o $TRIPLEO_ROOT/images/overcloud-cinder-volume \
	fedora cinder \
	neutron-openvswitch-agent heat-cfntools stackuser pip-cache
