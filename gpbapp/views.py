#! /usr/bin/env python
import json
from flask import Flask, render_template, request
from .utils.parserkiller import get_address
from .utils.googleapi import geocode_request
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
    return parserQuestion

@app.route('/wiki/<sentence>')
def wiki(sentence):
    geo = {}
    parserQuestion = get_address(sentence)
    geo["lat"], geo["lng"] = geocode_request(parserQuestion)
    print(geo)
    return json.dumps(geo)

#if __name__ == "__main__":
#    app.run()
