#!/usr/bin/python3
"""Class Rectangle not empty"""


class Rectangle:
    """Rectangle Class empty"""
    dict

    def __init__(self, width=0, height=0):
        """Something goes here"""
        self.height = height
        self.width = width

    @property
    def height(self):
        """Something goes here"""
        return self._height

    @height.setter
    def height(self, value):
        """Something goes here"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """Something goes here"""
        return self.__width

    @width.setter
    def width(self, value):
        """Something goes here"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
