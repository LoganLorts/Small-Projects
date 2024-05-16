# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
count = int(input('Enter count: '))
position = int(input('Enter position: '))
#html = urllib.request.urlopen(url, context=ctx).read()
#soup = BeautifulSoup(html, 'html.parser')
desired_string = (re.findall('by_(\S+)\.', url))
print(desired_string[0])
#print(tags)
for x in range(count):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    #print(tags)
    link = (tags[position-1].get('href', None))
    desired_string = (re.findall('by_(\S+)\.', link))
    print(desired_string[0])
    url = link
    