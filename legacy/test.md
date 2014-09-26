This element contains the common installation steps between RHEL os releases.

RHEL Registration
-----------------
This element provides functionality for registering RHEL images during the
image build process with the disk-image-create script from diskimage-builder.
The RHEL image will register itself with either the hosted Red Hat Customer
Portal or Satellite to enable software installation from official
repositories. After the end of the image creation process, the image will
unregister itself so an entitlement will not be decremented from the account.

Environment Variables For Image Creation
----------------------------------------
The following environment variables are used for registering a RHEL instance
with either the Red Hat Customer Portal or Satellite 6.

## REG\_ACTIVATION\_KEY
Attaches existing subscriptions as part of the registration process. The
subscriptions are pre-assigned by a vendor or by a systems administrator
using Subscription Asset Manager.

## REG\_AUTO\_ATTACH
Automatically attaches the best-matched compatible subscription. This is
good for automated setup operations, since the system can be configured
in a single step.

#### REG\_BASE\_URL
Gives the hostname of the content delivery server to use to receive updates.
Both Customer Portal Subscription Management and Subscription Asset Manager
use Red Hat's hosted content delivery services, with the URL
https://cdn.redhat.com. Since Satellite 6 hosts its own content, the URL
must be used for systems registered with Satellite 6.

#### REG\_ENVIRONMENT
Registers the system to an environment within an organization.

#### REG\_FORCE
Registers the system even if it is already registered. Normally, any register
operations will fail if the machine is already registered.

#### REG\_HALT\_UNREGISTER
At the end of the image build process, the element runs a cleanup script that
will unregister it from system it registered with.  There are some cases when
building an image where you may want to stop this from happening so you can
verify the registration or to build a one off-image where the boot-time
registration will not be enabled.  Set this value to '1' to stop the
unregistration process.

#### REG\_MACHINE\_NAME
Sets the name of the system to be registered. This defaults to be the same as
the hostname.

#### REG\_METHOD
Sets the method of registration.  Use "portal" to register a system with the
Red Hat Customer Portal.  Use "satellite" to register a system with Red
Hat Satellite 6.

#### REG\_ORG
Gives the organization to which to join the system.

#### REG\_PASSWORD
Gives the password for the user account.

#### REG\_RELEASE
Sets the operating system minor release to use for subscriptions for the
system. Products and updates are limited to that specific minor release
version. This is used only used with the REG_AUTO_ATTACH option.

#### REG\_REPOS
A single string representing a list of repository names separated by a
space.  Each of the repositories in this string are enabled through
subscription manager.

#### REG\_SERVER\_URL
Gives the hostname of the subscription service to use. The default is
for Customer Portal Subscription Management, subscription.rhn.redhat.com.
If this option is not used, the system is registered with Customer Portal
Subscription Management.

#### REG\_SERVICE\_LEVEL
Sets the service level to use for subscriptions on that machine. This
is only used with the REG_AUTO_ATTACH option.

#### REG\_USER
Gives the content server user account name.

#### REG\_TYPE
Sets what type of consumer is being registered. The default is system, which
is applicable to both physical systems and virtual guests. Other types include
hypervisor for virtual hosts, person, domain, rhui, and candlepin for some
subscription management applications.

Configuration
-------------
Heat metadata can be used to configure the rhel-common element.

    rh_registration:
        activation_key:
            # Attaches existing subscriptions as part of the registration
            # process. The subscriptions are pre-assigned by a vendor or by
            # a systems administrator using Subscription Asset Manager.
        auto_attach: 'true'
            # Automatically attaches the best-matched compatible subscription.
            # This is good for automated setup operations, since the system can
            # be configured in a single step.
        base_url:
            # Gives the hostname of the content delivery server to use to
            # receive updates.  Both Customer Portal Subscription Management
            # and Subscription Asset Manager use Red Hat's hosted content
            # delivery services, with the URL https://cdn.redhat.com. Since
            # Satellite 6 hosts its own content, the URL must be used for
            # systems registered with Satellite 6.
        environment:
            # Registers the system to an environment within an organization.
        force:
            # Registers the system even if it is already registered. Normally,
            # any register operations will fail if the machine is already
            # registered.
        machine_name:
            # Sets the name of the system to be registered. This defaults to be
            # the same as the hostname.
        org:
            # Gives the organization to which to join the system.
        password:
            # Gives the password for the user account.
        release:
            # Sets the operating system minor release to use for subscriptions
            # for the system. Products and updates are limited to that specific
            # minor release version. This is only used with the auto_attach
            # option.
        repos:
            # A single string representing a list of repository names separated
            # by a space.  Each of the repositories in this string are enabled
            # through subscription manager.
        satellite_url:
            # The url of the Satellite instance to register with.  Required for
            # Satellite registration.
        server_url:
            # Gives the hostname of the subscription service to use. The default
            # is for Customer Portal Subscription Management,
            # subscription.rhn.redhat.com. If this option is not used, the system
            # is registered with Customer Portal Subscription Management.
        service_level:
            # Sets the service level to use for subscriptions on that machine.
            # This is only used with the auto_attach option.
        user:
            # Gives the content server user account name.
        type:
            # Sets what type of consumer is being registered. The default is
            # "system", which is applicable to both physical systems and virtual
            # guests. Other types include "hypervisor" for virtual hosts,
            # "person", "domain", "rhui", and "candlepin" for some subscription
            # management applications.
        method:
            # Sets the method of registration.  Use "portal" to register a
            # system with the Red Hat Customer Portal.  Use "satellite" to
            # register a system with Red Hat Satellite 6.
