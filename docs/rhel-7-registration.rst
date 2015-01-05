RHEL 7 Registration Overview
================================
TODO: Add some info about registration process during image creation and during boot using customer portal or satellite6.

Building Images
===============================
TODO: Add info about adding metadata via REG_ env vars.
You'll need to start by downloading the rhel guest image and either uploading it to an http accessible location or use a local url (e.g. file:///)
Set the repos you'll need
create an regrc file with your settings

You'll need to export some environment variables
export NODE_DIST="rhel7"
export DIB_CLOUD_IMAGES="file:///home/stack"
# A cloud guest image downloaded from the Red Hat Customer Portal
export BASE_IMAGE_FILE="rhel-guest-image-7.0-20140930.0.x86_64.qcow2"
export REG_METHOD=portal
# Find this with `subscription-manager list --available`
export REG_POOL_ID="8a85f9823e3d5e43013e3e0af77e0f36"
#export REG_PASSWORD="mypassword"
#export REG_USER="myportalaccount"
export REG_REPOS="rhel-7-server-extras-rpms,rhel-ha-for-rhel-7-server-rpms,rhel-7-server-optional-rpms"

Satellite
export REG_METHOD=satellite
export REG_SAT_URL="http://satellite1.released-el6.satellite.lab.eng.rdu2.redhat.com"
export REG_ORG="ACME_Corporation"

--- options ---
Activation Key
export REG_ACTIVATION_KEY="rhel7-myCompany"
export REG_ORG="2794300"

User/Password
#export REG_PASSWORD="mypassword"
#export REG_USER="myportalaccount"





Booting Images
===============================
TODO: Add info about adding json metadata to env var for heat deployment of instack and through UI (tuskar)

Notes
===============================
If you're mixing and matching methods between image creation and boot time, you must set the server_url and base_url.


