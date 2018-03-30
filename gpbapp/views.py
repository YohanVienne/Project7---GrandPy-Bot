#! /usr/bin/env python
import json
from flask import Flask, render_template, request
from .utils.parserkiller import get_address
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
    print(parserQuestion)
    return parserQuestion

#if __name__ == "__main__":
#    app.run()
