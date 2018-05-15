import urllib
from BeautifulSoup import *
totalsum = 0
url = raw_input('Enter - ')

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

tags = soup("span",)

for tag in tags :
    val = tag.contents[0]
    totalsum += int(val)
print totalsum
raw_input("Continue...")
