#!/usr/bin/env python3
import requests, urllib3, json
urllib3.disable_warnings()

# set that content-type header, bud!
headers = {
    'Content-Type': 'application/json',
}

# get a list that's empty of the groups you'll find, bud!
netgroups = []
allhosts = []

# get yourself a session, bud!
data = open('auth.json')
r = requests.post('https://isicluster01:8080/session/1/session', headers=headers, data=data)

# get yourself some data, bud!
response = requests.get('https://isicluster01:8080/platform/1/protocols/nfs/exports', cookies=r.cookies)

data = json.loads(response.text)
for export in data['exports']:
    for item in export['root_clients']:
        print("Root access to export ID {} : {}".format(export['id'], item))
