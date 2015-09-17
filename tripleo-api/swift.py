#!/usr/bin/env python

import os
import fnmatch
import swiftclient


# this script verifies we have the necessary swift capabilities

def get_swiftclient():
    """ For this script, the authentication implementation is just the quickest
    means possible to a demonstration.
    """
    swift_conn = swiftclient.client.Connection(
        authurl=os.environ.get("OS_AUTH_URL"),
        user=os.environ.get("OS_USERNAME"),
        key=os.environ.get("OS_PASSWORD"),
        tenant_name=os.environ.get("OS_TENANT_NAME"),
        auth_version="2.0",
    )
    return swift_conn

# Plan existence functions

def create_plan(plan_name, templates_path):
    """Creates a plan by creating a Swift container matching plan_name, and
    placing the tripleo-heat-templates and an environment file into it.
    Although we will not deal with updates and versioning with this spec, we
    will create the Swift container with object versioning active to
    accommodate future development.
    http://docs.openstack.org/developer/swift/overview_object_versioning.html
    """
    swift = get_swiftclient()
    # create container
    client.put_container(plan_name, headers={'X-Versions-Location': 'versions'})
    # import templates
    matches = []
    for root, dirnames, filenames in os.walk(templates_path):
        for filename in fnmatch.filter(filenames, '*.yaml'):
            matches.append(os.path.join(root, filename))

    for template in matches:
        # get file path from root
        template_filename = template.replace(templates_path, '')
        # add file to swift container
        with open(template, 'rb') as target_file:
            file_contents = target_file.read()
            swift.put_object(plan_name, template_filename, file_contents)

    # create environment file & add to container
    overcloud_env_contents = '\n'.join([
        "# this is a test environment file.",
        "# had this been a real file, you would have resource_registry: and parameter_defaults: blocks",
        "\n"
    ])
    swift.put_object(plan_name, "%s-environment.yaml" % plan_name, overcloud_env_contents)


def delete_plan(plan_name):
    """Deletes a plan by deleting the Swift container matching plan_name."""
    swift = get_swiftclient()
    # delete files from plan
    for data in swift.get_container(plan_name)[1]:
        swift.delete_object(plan_name, data['name'])
    # delete plan container
    swift.delete_container(plan_name)

# end plan existence functions

# Deployment Options

def get_deployment_template_resource_types(plan_name):
    """Determine available template resource types by retrieving plan_name's
    templates from Swift and using the proposed Heat resource-capabilities API
    (https://review.openstack.org/#/c/196656/7/specs/liberty/resource-capabilities.rst)."""
    pass


def update_deployment_template_resource_types(plan_name, resource_types):
    """Retrieve plan_name's environment file from Swift and update the
    resource_registry tree according to the values passed in by resource_types.
    Then update the environment file in Swift.
    """
    pass

# end deployment options

# Deployment Configuration functions

def get_deployment_parameters(plan_name):
    """Determine available deployment parameters by retrieving plan_name's
    templates from Swift and using the proposed Heat nested-validation API
    call (https://review.openstack.org/#/c/197199/5/specs/liberty/nested-validation.rst).
    """
    pass


def update_deployment_parameters(plan_name, deployment_parameters=None):
    """Retrieve plan_name's environment file from Swift and update the parameters
    according to the values passed in by deployment_parameters.  Then update the
    environment file in Swift.
    """
    if deployment_parameters:
        swift = get_swiftclient()
        obj_tuple = swift.get_object(plan_name, "%s-environment.yaml" % plan_name)
        # TODO: update the values coming from obj_tuple[1]
        overcloud_env_contents = obj_tuple[1]
        swift.put_object(plan_name, "%s-environment.yaml" % plan_name, overcloud_env_contents)


def get_deployment_roles(plan_name):
    """Determine available deployment roles. This can be done by retrieving
    plan_name's deployment parameters and deriving available roles from
    parameter names; or by looking at the top-level ResourceGroup types.
    """
    pass

# end deployment configuration

# Deployment

def validate_plan(plan_name):
    """Retrieve plan_name's templates and environment file from Swift and use
    them in a Heat API validation call.
    """
    pass

def deploy_plan(plan_name):
    """Retrieve plan_name's templates and environment
    file from Swift and use them in a Heat API call to create the overcloud
    stack.  Perform any needed pre-processing of the templates, such as the
    template file dictionary needed by Heat.  This function will return a Heat
    stack ID that can be used to monitor the status of the deployment.
    """
    pass

# end deployment

#  Post-Deploy

def postdeploy_plan(plan_name):
    """ Initialize the API endpoints of the overcloud corresponding to
    plan_name.
    """
    pass

# end post-deploy

if __name__ == "__main__":

    test_container = "overcloud"
    test_filename = 'test-environment.txt'
    client = get_swiftclient()
    # List the containers
    print("Container List")
    print(client.head_account())

    create_plan(test_container, '/usr/share/openstack-tripleo-heat-templates/')

    # print("Adding file to container")
    # Add files to swift container
    # with open(test_filename, 'rb') as f:
    #    file_data = f.read()
    #    client.put_object(test_container, test_filename, file_data)

    print("Listing files in container")
    for data in client.get_container(test_container)[1]:
        print '{0}\t{1}\t{2}'.format(data['name'], data['bytes'], data['last_modified'])

    print("Getting file from container")
    # Retrieve files from swift container
    obj_tuple = client.get_object(test_container, "%s-environment.yaml" % test_container)
    with open("edit-%s" % test_filename, 'w') as test_file:
        test_file.write(obj_tuple[1])

    # Edit file and update file in swift container
    with open("edit-%s" % test_filename, 'rb') as target_file:
        file_contents = target_file.read()
        client.put_object(test_container, "edit-%s" % test_filename, file_contents)

    print("Listing files in container")
    # List container contents
    for data in client.get_container(test_container)[1]:
        print '{0}\t{1}\t{2}'.format(data['name'], data['bytes'], data['last_modified'])

    print("Deleting container")
    # Delete swift container
    delete_plan(test_container)

    print("Container List")
    # List the containers
    print(client.head_account())

