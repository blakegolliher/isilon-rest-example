#!/usr/local/python-2.7.2/bin/python

import urllib2

# change the hostname
response = urllib2.urlopen('https://yoyo.isi.pitythefoo.com:9443/1/stats/history?key=node.cpu.user.avg&devid=all&degraded=1&interval=25&memory_only=1&begin=1371759481')
out = response.read()

# URL
print "The URL is: ", response.geturl()

# resp code
print "This gets the code: ", response.code

# date
print "The Date is: ", response.info()['date']

# data - yay
print "Get all data: ", out

# lenth
print "Get the length :", len(out)
