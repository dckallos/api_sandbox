import json
import os

## Import URL Information
def get_endpoints():
    cfg = json.load(open(os.getcwd()+'/config/configure_endpoints.json'))
    google_endpoint = cfg['GOOGLE']
    foursquare_endpoint = cfg['FOURSQUARE']
    return(google_endpoint, foursquare_endpoint)

def get_google_key():
    cfg = json.load(open(os.getcwd()+'/config/configure_tokens.json'))
    google_api_key = cfg['ENDPOINTS'][0]['GOOGLE']['GEOCODE']
    return(google_api_key)

def get_foursquare_keys():
    cfg = json.load(open(os.getcwd()+'/config/configure_tokens.json'))
    fs_client_id = cfg['ENDPOINTS'][1]['FOURSQUARE']['CLIENT_ID']
    fs_client_secret = cfg['ENDPOINTS'][1]['FOURSQUARE']['CLIENT_SECRET']
    return(fs_client_id, fs_client_secret)

print get_foursquare_keys()
    
