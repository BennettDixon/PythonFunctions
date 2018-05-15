import urllib
from BeautifulSoup import *
urllist = []
url = raw_input('Enter URL - ')
count = raw_input("Enter Count - ")
position = raw_input('Enter Position - ')
x = 0
while x < int(count) :
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    tags = soup("a")
    for tag in tags :
        urllist.append(tag.get('href', None))
    url = urllist[(int(position)-1)]
    print "Retrieving : " + url
    urllist[:] = []
    x += 1
    print x

raw_input("Continue...")
