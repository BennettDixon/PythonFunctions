import json
import urllib
totalsum = 0
url = raw_input("Enter URL: ")
response = urllib.urlopen(url)
data = response.read()

js = json.loads(data)


for item in js["comments"] :
    count = item["count"]
    totalsum += int(count)
print totalsum
raw_input("Continue...")
