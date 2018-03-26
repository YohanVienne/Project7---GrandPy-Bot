#!/usr/bin/python

# Pytest file
from gpbapp.utils.googleapi import geocode_request

def test_get_coordinate_position():
    """ get the coordinate X and Y from the user address """
    assert geocode_request("7 rue des champs, Paris") == (
        48.8506544, 2.3998547)
