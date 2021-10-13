#!/usr/bin/python3
""" Module save python object to JSON model in file """
import json


def save_to_json_file(my_obj, filename):
    """ save to json file implementation """
    with open(filename, "w", encoding="utf-8") as myfile:
        json.dump(my_obj, myfile)
