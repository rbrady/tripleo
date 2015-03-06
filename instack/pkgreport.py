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
    return repoquery.replace("\n", "").split('|')


def main():
    print("Retrieving list of RDO Management Delorean Packages")
    rmd = get_packages_from_directory_listing(rdo_delorean_uri)
    raw_data = dict()
    requery = dict()
    not_found = []
    for package in rmd:
        try:
            pkg = check_package_source_repo(package)
            raw_data.update({pkg[1]: pkg[0]})
        except:
            # try to follow up with an additional query
            # maybe the version or something else is off
            # between the installed package and the package
            # from the repo.  The package names use hypens,
            # lets grab the first couple of segments and see
            # if that does any better.
            try:
                partial_name = '-'.join([segment for segment in package.split('-') if segment.isalpha()])
                print("Second chance lookup for %s" % partial_name)
                pkg = check_package_source_repo(partial_name)
                requery.update({pkg[1]: pkg[0]})
            except:
                # if all else fails, notify user of scripts failure
                not_found.append(package)

    rpt_data = {}
    for k, v in raw_data.iteritems():
        rpt_data.setdefault(v, []).append(k)

    for k, v in rpt_data.iteritems():
        print("\n** %s Packages **" % k)
        for sorted_pkg in v:
            print(sorted_pkg)

    if len(requery) > 0:
        print("The following packages may not be the same version as found in the delorean repo.")
        print(requery)

    if len(not_found) > 0:
        print("%d packages were not found" % len(not_found))
        for orphan in not_found:
            print(orphan)


if __name__ == "__main__":
    main()
