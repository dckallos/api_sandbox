import json
import requests
import httplib2
import common
import sys

## Import functions from code directory
sys.path.insert(0, '/code')
import common


def define_geocode_location(location_string):
    
    location_string = location_string.replace(' ','+')
    url = common.import_endpoints()[0]
    full_url = (url+'?address=%s&key=%s' % (
        location_string, common.import_google_key()
    ))
    h = httplib2.Http()
    [response, content] = h.request(full_url, 'GET')
    result = json.loads(content)
    return result

def query_foursquare_recommendation(location_string, search_interest):

    coord_string = common.parse_coordinates(
        define_geocode_location(location_string)
    )
    fs_parameters = dict(
        client_id=common.import_foursquare_keys()[0],
        client_secret=common.import_foursquare_keys()[1],
        v='20170801',
        ll=coord_string,
        query=search_interest,
        limit=1
    )
    response = requests.get(
        url=common.import_endpoints()[1], params=fs_parameters
    )
    result = json.loads(response.text)
    return(result)

x = query_foursquare_recommendation('Kalamazoo,MI','coffee')
print json.dumps(x, sort_keys=True, indent=4)