import xml.etree.ElementTree as ET
import urllib.request, urllib.parse, urllib.error

url = input('Enter location')
data = urllib.request.urlopen(url).read()
tree = ET.fromstring(data)

sum = 0
counts = (tree.findall('.//count'))
for count in counts:
    sum += int(count.text)
print(sum)