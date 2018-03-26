#! /usr/bin/env python
from flask import Flask, render_template
from .utils.googleapi import geocode_request
app = Flask(__name__)

# Add config.py file
app.config.from_object('config')

@app.route('/')
def index():
    #coor_lat, coor_lng = geocode_request()
    coor_lat = 48.8506544
    coor_lng = 2.3998547
    return render_template("index.html",
                           coor_lat=coor_lat,
                           coor_lng=coor_lng)

#if __name__ == "__main__":
#    app.run()
