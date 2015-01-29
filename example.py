import wadllib
import os
import pkg_resources

from wadllib.application import Application

#
# Example from https://pypi.python.org/pypi/wadllib/1.1.5
# Copyright applies as stated.
#

# Application for a wadl object
wadl_string = pkg_resources.resource_string('wadllib.tests.data','launchpad-wadl.xml')
wadl = Application("http://api.launchpad.dev/beta/", wadl_string)

def application_for(filename, url="http://localhost/"):
    wadl_stream = pkg_resources.resource_stream('tests.data',filename)
    return Application(url, wadl_stream)

filename = "launchpad-wadl.xml"
wadl = application_for(filename,"http://api.launchpad.dev/beta/")
print "wadl: ",wadl

# Link Navigation

# The preferred technique for finding a resource is to start at one of
# the resources defined in the WADL file, and follow links. This code
# retrieves the definition of the root resource.
service_root = wadl.get_resource_by_path('')
print "service root: ",service_root.url
print "type url: ",service_root.type_url

# The service root resource supports GET.
get_method = service_root.get_method('GET')
print "id: ",get_method.id
print "method name: " + get_method.name

# Get restapi method url
print "url: ",get_method.build_request_url()


