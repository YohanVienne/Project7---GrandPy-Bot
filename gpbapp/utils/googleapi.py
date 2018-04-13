#!/usr/bin/python
import config
import requests


url = "https://maps.googleapis.com/maps/api/geocode/json"

def geocode_request(userAddress):
    """ Request the Google Geocode API pour lat/lng position """
    payload = {'address': userAddress, 'key': config.GOOGLE_APP_ID}
    req = requests.get(url, params=payload)
    if req.status_code == 200:
        if req:
            result = req.json()
            print(result["results"][0]['geometry']['location']['lat'])
            print(result["results"][0]['geometry']['location']['lng'])
            coordinate_lat = result["results"][0]['geometry']['location']['lat']
            coordinate_lng = result["results"][0]['geometry']['location']['lng']
            return coordinate_lat, coordinate_lng
        else:
            return "none"
    else:
        print("The Geo_Code request has failed with the html error:" +
              str(req.status_code))
