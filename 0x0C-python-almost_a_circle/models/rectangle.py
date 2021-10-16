#!/usr/bin/python3
""" Model rectangle """
from .base import Base

class Rectangle(Base):
    """ Class Rectangle inherits from Base """

    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not type(value) == int:
            raise TypeError("width must be an integer")
        if value <=0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self._y = value
