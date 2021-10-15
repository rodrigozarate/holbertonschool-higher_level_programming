#!/usr/bin/python3
""" Module base clase """


class Base:
    """ Class Base """

    def __init__(self, id=None):
        """ definition of instance atributes """
        self.__nb_objects = 0
        if not self.id == None:
            self.id = self.id
        else
            self.__nb_objects += 1
            self.id = __nb_objects
