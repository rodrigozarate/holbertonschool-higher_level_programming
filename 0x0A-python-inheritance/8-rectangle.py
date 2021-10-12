#!/usr/bin/python3
""" Module rectangle """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Class rectangle inherit Base geometry """
    def __init__(self, width, height):
        """ Rectangle size init """
        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height
