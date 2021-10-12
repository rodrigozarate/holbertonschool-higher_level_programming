#!/usr/bin/python3
""" Module create python object from JSON model in file """
import json


def load_from_json_file(filename):
    with open(filename, "r", encoding="utf-8") as myfile:
        return json.load(myfile)
