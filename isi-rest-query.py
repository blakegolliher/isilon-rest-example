#!/usr/local/python-2.7.2/bin/python

import sys, urllib, urllib2, json, time
from pprint import pprint

cluster_name = sys.argv[1]

NOW = int(time.time())
NOW -= 30
RIGHTNOW = ('%.0f' % NOW)

baseurl = 'https://%s:9443/1/stats/history?' % cluster_name
queryargs = { 'key':'node.disk.xfers.rate.avg', 'devid':'all', 'degraded':1, 'interval':25, 'memory_only':1, 'begin':RIGHTNOW }
urlquery = baseurl + urllib.urlencode(queryargs)
print "urlquery is      : %s" % urlquery
request = urllib2.Request(urlquery)
response = urllib2.urlopen(request)

out = response.read()

# URL
print "The URL is: ", response.geturl()

# resp code
print "This gets the code: ", response.code

# data - yay
print "Get all data: ", out

# lenth
print "Get the length :", len(out)

# load in json, and print it
jsondata = json.loads(out)
pprint(jsondata)
