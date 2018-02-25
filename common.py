import json
import os

## Import URL Information
def import_endpoints():
    cfg = json.load(open(os.getcwd()+'/config/configure_endpoints.json'))
    google_endpoint = cfg['GOOGLE']
    foursquare_endpoint = cfg['FOURSQUARE']
    return(google_endpoint, foursquare_endpoint)

def import_google_key():
    cfg = json.load(open(os.getcwd()+'/config/configure_tokens.json'))
    google_api_key = cfg['ENDPOINTS'][0]['GOOGLE']['GEOCODE']
    return(google_api_key)

def import_foursquare_keys():
    cfg = json.load(open(os.getcwd()+'/config/configure_tokens.json'))
    fs_client_id = cfg['ENDPOINTS'][1]['FOURSQUARE']['CLIENT_ID']
    fs_client_secret = cfg['ENDPOINTS'][1]['FOURSQUARE']['CLIENT_SECRET']
    return(fs_client_id, fs_client_secret)

def parse_coordinates(google_json_response):
    lat = google_json_response['results'][0]['geometry']['location']['lat']
    lng = google_json_response['results'][0]['geometry']['location']['lng']
    coord_string = '%s,%s' % (lat, lng)
    return(coord_string)
    
