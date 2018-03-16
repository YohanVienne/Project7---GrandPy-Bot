#!/usr/bin/python
"""
Parserkiller get the question of user and parser it to get the adress for Google map API

Author : Yohan Vienne
version : 0.1
"""

import json, os, re, io



class ParserKiller:
    ''' Get the adress from the user question '''

    def __init__(self):
        self.json_file = 'gpbapp/utils/stop_words_fr.json'

    def _get_stopwords_list(self):
        """ Get the stop words list for parser """
        json_output = json.load(io.open(self.json_file, 'r', encoding='utf-8-sig'))
        json_output.sort()
        return json_output
    
    def _split_user_question(self, user_question):
        """ Split the user question in a list """
        user_question = user_question.lower()
        parse_list_question = re.split(r'\W+', user_question)
        return parse_list_question

    def get_adress(self, user_question):
        """ Parse the user question to extract the adress """
        list_sentence = self._split_user_question(user_question)
        dict_list = self._get_stopwords_list()
        output_answer = ''
        sequence = ' '
        try:
            for stopWords in dict_list:
                for word in list_sentence:
                    if word == stopWords:
                        list_sentence.remove(word)
                        continue
            output_answer = sequence.join(list_sentence).strip(' ')
        except Exception:
            output_answer = "Je n'ai pas compris ta question "

        return output_answer