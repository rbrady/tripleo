#!/usr/bin/env python
import lxml.html
import requests
from subprocess import check_output

rdo_delorean_uri = "http://trunk-mgt.rdoproject.org/repos/current/"
core_delorean_uri = "http://104.130.230.24/centos70/current/"
queryformat = "%{repoid}|%{name}-%{version}-%{release}"


def get_packages_from_directory_listing(list_uri):
    r = requests.get(list_uri)
    dom = lxml.html.fromstring(r.text)
    return [link.replace('.noarch.rpm', '').replace('.src.rpm', '') for link in dom.xpath('//a/@href') if link.endswith('.rpm')]


def check_package_source_repo(package_name):
    repoquery = check_output(['repoquery', package_name, '--queryformat', queryformat])
    if repoquery == '':
        return None
    return repoquery.replace("\n", "").split('|')


def get_package_name(package):
    return '-'.join([segment for segment in package.split('-') if segment.isalpha()])


def main():
    print("Retrieving list of RDO Management Delorean Packages")
    rmd = get_packages_from_directory_listing(rdo_delorean_uri)
    core = get_packages_from_directory_listing(core_delorean_uri)
    print("Retrieved %d packages from rdo-mgt-delorean" % len(rmd))
    print("Retrieved %d packages from delorean" % len(core))
    expected = {}
    for item in rmd:
        actual = check_package_source_repo(get_package_name(item))
        status = "not installed"
        repo = ''
        package = ''
        if not actual is None:
            status = 'installed'
            repo = actual[0]
            package = actual[1]

        expected[get_package_name(item)] = {
            'expected': {
                'repo': 'delorean-rdo-management',
                'package': item,
            },
            'actual': {
                'repo': repo,
                'package': package,
                'status': status,
            }
        }

    for item in core:
        name = get_package_name(item)
        if not name in set(expected.keys()):
            actual = check_package_source_repo(name)
            status = "not installed"
            repo = ''
            package = ''
            if not actual is None:
                status = 'installed'
                repo = actual[0]
                package = actual[1]

            expected[name] = {
                'expected': {
                    'repo': 'delorean',
                    'package': item,
                },
                'actual': {
                    'repo': repo,
                    'package': package,
                    'status': status,
                }
            }

    for k,v in expected.iteritems():
        print(k) # package level
        for kk,vv in v.iteritems():
            print(kk) # expected|actual
            for kkk,vvv in vv.iteritems():
                print("%s:  %s" % (kkk,vvv))
        print("\n")


if __name__ == "__main__":
    main()
