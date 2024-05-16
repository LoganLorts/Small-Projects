import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input('Enter location: ')
key = 42
service_url = 'http://py4e-data.dr-chuck.net/json?'
parms = dict()
parms['address'] = address
parms['key'] = key
url = service_url + urllib.parse.urlencode(parms)

site_data = urllib.request.urlopen(url)
data = site_data.read().decode()
json_data = json.loads(data)
print(json_data['results'][0]['place_id'])
#print(data)

