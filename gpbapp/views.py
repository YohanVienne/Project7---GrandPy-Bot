#! /usr/bin/env python
import json, random

import requests
from flask import Flask, render_template, request
from .utils.parserkiller import get_address
from .utils.googleapi import geocode_request
from .utils.wikiapi import req_wikimedia
from .utils.wikiapi import req_story

app = Flask(__name__)

# Add config.py file
app.config.from_object('config')

@app.route('/')
@app.route('/index/')
def index():
    return render_template("index.html")


@app.route('/question/<sentence>')
def question(sentence):
    """Get the user question, parse it and show the address on map"""
    parserQuestion = get_address(sentence)
   
    # Get location for Google Map API marker
    geoLat, geoLng = geocode_request(parserQuestion)
    print("Google location: " + str(geoLat) + ", " +str(geoLng))

    # Get random story & title for Wiki Media API
    wikiLocation = str(geoLat) + "|" + str(geoLng)
    print("Wiki location: " + wikiLocation)
    wikiRequest = req_wikimedia(wikiLocation)
    lenResult = len(wikiRequest['query']['geosearch'])
    print("lenResult = " + str(lenResult))
    if lenResult >=1:
        ranStory = random.randrange(lenResult)
        print("ran = " + str(ranStory))
        story = req_story(wikiRequest, ranStory)
    else:
        story = "Je ne me rapelle de rien concernant ce lieux..."
        title = ""
    
    # Build the Json result to return
    data = {}
    data['lat'] = geoLat
    data['lng'] = geoLng
    if lenResult >=1:
        data['title'] =  story[0]['title']
        data['story'] = story[0]['extract']
    else:
        data['title'] = title
        data['story'] = story
    jsonData = json.dumps(data, ensure_ascii=False, indent=4)
    print("jsonData: " + str(jsonData))
    return jsonData

    
