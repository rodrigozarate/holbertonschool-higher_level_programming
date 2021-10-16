#!/usr/bin/python3
""" Model rectangle """


class Rectangle(Base):
    """ Class Rectangle inherits from Base """
    __width -> width
    __height -> height
    __x -> x
    __y -> y

    def __init__(self, width, height, x=0, y=0, id=None)
        self.__width = width
        self.__height = height
        self.__x = 0
        self.__y = 0

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value
