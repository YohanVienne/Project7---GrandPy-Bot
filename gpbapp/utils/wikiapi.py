#!/usr/bin/python
''' 
Wiki Media API module
Author: Yohan Vienne
Version: 1.0
'''

import json
import requests

url = "https://fr.wikipedia.org/w/api.php"

def req_wikimedia(wikiLocation):
    ''' Request the API with location, get some page around the location,
    get a random page in result and return to the HTML page'''
    payload = {'action': 'query', 'format': 'json', 'uselang': 'fr',
                'list': 'geosearch', 'gscoord': wikiLocation}
    req = requests.get(url, params=payload)
    if req.status_code == 200:
        wikiReq = req.json()
    else:
        print("The Wiki request has failed with the html error:" + str(req.status_code))
    return wikiReq

def req_story(wikiRequest, ranStory):
    ''' Get a random story from the geosearch'''
    pageId = wikiRequest['query']['geosearch'][ranStory]['pageid']
    payload = {'action': 'query', 'format': 'json', 'prop': 'extracts',
                'utf8': '1', 'formatversion': 'latest', 'exsentences': '3',
                'explaintext': '1', 'exsectionformat': 'wiki', 'pageids': pageId}
    req = requests.get(url, params=payload)
    if req.status_code == 200:
        result = req.json()
        wikiReq = result['query']['pages']
    else:
        print("The Wiki request has failed with the html error:" + str(req.status_code))
    return wikiReq

#if __name__ == "__main__":
#    pass
