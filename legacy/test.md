Configuration
-------------
rh_registration:
    activation_key:
        -   Attaches existing subscriptions as part of the registration
            process. The subscriptions are pre-assigned by a vendor or by
            a systems administrator using Subscription Asset Manager.
    auto_attach: 'true'
        -   Automatically attaches the best-matched compatible subscription.
            This is good for automated setup operations, since the system can
            be configured in a single step.
    base_url:
        -   Gives the hostname of the content delivery server to use to
            receive updates.  Both Customer Portal Subscription Management
            and Subscription Asset Manager use Red Hat's hosted content
            delivery services, with the URL https://cdn.redhat.com. Since
            Satellite 6 hosts its own content, the URL must be used for
            systems registered with Satellite 6.
    environment:
        -   Registers the system to an environment within an organization.
    force:
        -   Registers the system even if it is already registered. Normally,
            any register operations will fail if the machine is already
            registered.
    machine_name:
        -   Sets the name of the system to be registered. This defaults to be
            the same as the hostname.
    org:
        -   Gives the organization to which to join the system.
    password:
        -   Gives the password for the user account.
    release:
        -   Sets the operating system minor release to use for subscriptions
            for the system. Products and updates are limited to that specific
            minor release version. This is only used with the auto_attach
            option.
    repos:
        -   A single string representing a list of repository names separated
            by a space.  Each of the repositories in this string are enabled
            through subscription manager.
    satellite_url:
        -   The url of the Satellite instance to register with.  Required for
            Satellite registration.
    server_url:
        -   Gives the hostname of the subscription service to use. The default
            is for Customer Portal Subscription Management,
            subscription.rhn.redhat.com. If this option is not used, the system
            is registered with Customer Portal Subscription Management.
    service_level:
        -   Sets the service level to use for subscriptions on that machine.
            This is only used with the auto_attach option.
    user:
        -   Gives the content server user account name.
    type:
        -   Sets what type of consumer is being registered. The default is
            "system", which is applicable to both physical systems and virtual
            guests. Other types include "hypervisor" for virtual hosts,
            "person", "domain", "rhui", and "candlepin" for some subscription
            management applications.
    method:
        -   Sets the method of registration.  Use "portal" to register a
            system with the Red Hat Customer Portal.  Use "satellite" to
            register a system with Red Hat Satellite 6.
