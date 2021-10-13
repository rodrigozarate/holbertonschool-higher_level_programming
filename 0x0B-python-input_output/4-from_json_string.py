#!/usr/bin/python3
""" Module JSON string to python object """
import json


def from_json_string(my_str):
    """ from json to string implementation """
    return json.loads(my_str)
