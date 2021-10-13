#!/usr/bin/python3
""" Module definition of student class """


class Student():
    """ Class to define a student """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if type(attrs) is list and all([type(x) == str for x in attrs]):
            return {key: value for key, value
                    in self.__dict__.items() if key in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        for i, j in json.items():
            self.__dict__[i] = j
