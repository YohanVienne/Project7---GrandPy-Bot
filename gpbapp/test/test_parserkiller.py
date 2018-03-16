#!/usr/bin/python

# Pytest file
import gpbapp.utils.parserkiller as script

# Parserkiller test

pk = script.ParserKiller()

def test_get_stopwords_file():
    """ Get the stop word list """
    assert type(pk._get_stopwords_list()) == list

def test_split_the_user_question():
    """ Split the question in list """
    assert pk._split_user_question("J'ai été au 7 rue des champs à Paris avant hier") == [
        "j", "ai", "été", "au", "7", "rue", "des", "champs", "à", "paris", "avant", "hier"]

def test_compare_the_user_sentence_to_dict_list():
    """ Compare the user_sentence to the stop words list """
    assert pk.get_adress("J'ai été au 7 rue des champs à Paris avant hier") == "7 rue des champs paris"
    assert pk.get_adress("Ou est la Tour Eiffel ?") == "tour eiffel"
    assert pk.get_adress("Sais tu où est le Ministère de la défense ?") == "ministère défense"

    
