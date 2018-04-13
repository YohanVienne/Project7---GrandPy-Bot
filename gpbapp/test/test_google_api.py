#!/usr/bin/python

# Pytest file
from gpbapp.utils.googleapi import geocode_request

import requests
import requests_mock
import config

def test_geocode_request():
    """ Request the Geocode API to get the position for the map """
    result = {'results': [{'address_components': [{'long_name': 'Paris',
                'short_name': 'Paris', 'types': ['locality', 'political']},
                {'long_name': 'Paris', 'short_name': 'Paris',
                'types':['administrative_area_level_2', 'political']},
                {'long_name': 'Île-de-France', 'short_name': 'Île-de-France',
                'types': ['administrative_area_level_1', 'political']},
                {'long_name': 'France', 'short_name': 'FR',
                'types': ['country', 'political']}],
                'formatted_address': 'Paris, France',
                'geometry': {'bounds': {'northeast': {'lat': 48.9021449, 'lng': 2.4699208},
                'southwest': {'lat': 48.815573, 'lng': 2.224199}},
                'location': {'lat': 48.856614, 'lng': 2.3522219},
                'location_type': 'APPROXIMATE',
                'viewport': {'northeast': {'lat': 48.9021449, 'lng': 2.4699208},
                'southwest': {'lat': 48.815573, 'lng': 2.224199}}},
                'place_id': 'ChIJD7fiBh9u5kcRYJSMaMOCCwQ',
                'types': ['locality', 'political']}], 'status': 'OK'}

    with requests_mock.Mocker() as m:
        m.get('https://maps.googleapis.com/maps/api/geocode/json?address=paris&key=' + config.GOOGLE_APP_ID, json=result)
        req = geocode_request('paris')
        assert req == (48.856614, 2.3522219)
