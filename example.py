# Examples from [bazaar.launchpad.net](http://bazaar.launchpad.net/~lazr-developers/wadllib/trunk/view/head:/src/wadllib/README.txt)

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

# In this case the server has a JSON representation
def test_raises(exc_class, method, *args, **kwargs):
    try:
        method(*args, **kwargs)
    except Exception:
    # Contortion to support Python < 2.6 and >= 3 simultaneously.
        e = sys.exc_info()[1]
        if isinstance(e, exc_class):
            print(e)
            return
        raise
    raise Exception("Expected exception %s not raised" % exc_class)

# You can't bind just any representation to a WADL resource description.
# It has to be of a media type understood by the WADL description.

json_representation = service_root.get_representation_definition('application/json')
print "json_representation.media_type: ", json_representation.media_type

# We use test JSON data from a file to simulate the result of a GET request to the service root.
def get_testdata(filename):
    return pkg_resources.resource_string('wadllib.tests.data', filename + '.json')

def bind_to_testdata(resource, filename):
    return resource.bind(get_testdata(filename), 'application/json')

# The return value is a new Resource object that's "bound" to that JSON test data.
bound_service_root = bind_to_testdata(service_root, 'root')
print "for all param in bound_service_root.parameters: ", sorted([param.name for param in bound_service_root.parameters()])

print "sorted(bound_service_root.bound_service_root.parameters()): ", sorted(bound_service_root.parameters())

print "iter: ", [method.id for method in bound_service_root.method_iter]
