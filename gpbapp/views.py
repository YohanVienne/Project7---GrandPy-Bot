#! /usr/bin/env python
import json
from flask import Flask, render_template, request
from .utils.googleapi import geocode_request
from .utils.parserkiller import get_address
app = Flask(__name__)

# Add config.py file
app.config.from_object('config')


@app.route('/')
@app.route('/index/')
def index():
    return render_template("index.html")


@app.route('/question', methods=['POST'])
def question():
    """Get the user question, parse it and show the address on map"""
    question = request.form['question']
    parserQuestion = get_address(question)
    print(parserQuestion)
    return "OK"

#if __name__ == "__main__":
#    app.run()
