import json
import urllib.request, urllib.parse, urllib.error
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url: ')
if len(url) < 1:
    print('invalid url')
    exit()

info = urllib.request.urlopen(url)
data = info.read().decode()
js = json.loads(data)
sum = 0
#print(json.dumps(js, indent=4))
for entry in js['comments']:
    num = (entry["count"])
    #print(num)
    sum += int(num)
print(sum)