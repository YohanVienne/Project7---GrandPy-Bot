#!/usr/bin/python
"""
Parserkiller get the question of user and parser it to get the adress for Google map API

Author : Yohan Vienne
version : 0.1
"""

import json, os, re, io


#Get the stopWords json into a list 
json_file = 'gpbapp/utils/stop_words_fr.json'

def get_stopwords_list():
    """ Get the stop words list for parser """
    json_output = json.load(io.open(json_file, 'r', encoding='utf-8-sig'))
    json_output.sort()
    return json_output

def split_user_question(user_question):
    """ Split the user question in a list """
    user_question = user_question.lower()
    parse_list_question = re.split(r'\W+', user_question)
    return parse_list_question

def get_address(user_question):
    """ Parse the user question to extract the adress """
    output_address = []
    list_sentence = split_user_question(user_question)
    dict_list = set(get_stopwords_list())
    output_address = ' '.join(
        [word for word in list_sentence if word not in dict_list]).strip(' ')
    return output_address