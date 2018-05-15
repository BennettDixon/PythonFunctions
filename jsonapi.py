import urllib
import json

api_url = 'http://python-data.dr-chuck.net/geojson?'

while True:
    location = raw_input('Enter a location: ')
    if len(location) < 1 : break

    url = api_url + urllib.urlencode({'sensor' : 'false', 'address' : location})
    print 'Retrieving', urllib
    response = urllib.urlopen(url)
    data = response.read()
    print 'Retrieved',len(data),'characters'

    try: js = json.loads(str(data))
    except: js = None
    print json.dumps(js, indent=4)
    place_id = js["results"][0]["place_id"]
    print place_id
raw_input("Continue...")
