import urllib
import xml.etree.ElementTree as ET
totalsum = 0

url = raw_input("Enter URL to be parsed: ")
response = urllib.urlopen(url)
xml_data = response.read()
print "Fetched",len(xml_data),"characters"
tree = ET.fromstring(xml_data)

for element in tree.findall('.//comment'):
	count_ = element.find('count').text
	totalsum += int(count_)
print totalsum
raw_input("Continue...")
