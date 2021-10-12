#!/usr/bin/python3
""" Module test for inherited instance of class """


def inherits_from(obj, a_class):
    """ Compare object to verfy if is instance of class """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
