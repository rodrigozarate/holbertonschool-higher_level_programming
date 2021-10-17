#!/usr/bin/python3
""" Module base clase """
import json


class Base:
    """ Class Base """
    __nb_objects = 0

    def __init__(self, id=None):
        """ definition of instance atributes """
        if not id == None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
        def to_json_string(list_dictionaries):
            if not list_dictionaries:
               return "[]"
            return json.dumps(list_dictionaries)
