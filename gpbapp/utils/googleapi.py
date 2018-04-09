#!/usr/bin/python
import googlemaps
import config

gmaps = googlemaps.Client(key=config.GOOGLE_APP_ID)

def geocode_request(user_address):
    """ Get coordinate from Geocoding API with the parser user question """
    geo_result = gmaps.geocode(user_address)
    if geo_result:
        print("geo_result: " + str(geo_result))
        coordinate_lat = geo_result[0]["geometry"]["location"]["lat"]
        coordinate_lng = geo_result[0]["geometry"]["location"]["lng"]
        return coordinate_lat, coordinate_lng
    else:
        return "none"