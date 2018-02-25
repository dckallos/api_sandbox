import json
import requests
import httplib2
import common

def get_geocode_location(query_string):
    
    location_string = query_string.replace(' ','+')
    url = common.get_endpoints()[0]
    full_url = (url+'?address=%s&key=%s' % (
        location_string, common.get_google_key()
    ))
    h = httplib2.Http()
    [response, content] = h.request(full_url, 'GET')
    result = json.loads(content)
    #print('response header: %s \n \n' % response)
    return result

x = get_geocode_location('Kalamazoo,MI')
#print x['results'][]
#print json.dumps(x, sort_keys=True, indent=4)
#TODO: ENSURE THAT THIS IS PART OF THE FIRST FUNCTION
lat = x['results'][0]['geometry']['location']['lat']
lng = x['results'][0]['geometry']['location']['lng']
print('lat = %s') % lat 
print('lng = %s') % lng

#TODO: FORMAT AS A FUNCTION, NOT AS INLINE

lat_test = '42.29'
lng_test = '-85.58'
string_test = '%s,%s' % (lat_test, lng_test)
#print string_test

params = dict(
  client_id=common.get_foursquare_keys()[0],
  client_secret=common.get_foursquare_keys()[1],
  v='20170801',
  ll=string_test,
  query='coffee',
  limit=1
)
resp = requests.get(url=common.get_endpoints()[1], params=params)
data = json.loads(resp.text)
print json.dumps(data, sort_keys=True, indent=4)