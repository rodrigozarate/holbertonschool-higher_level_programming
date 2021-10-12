#!/usr/bin/python3
""" Module square inherit from rectangle """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Class Square """
    def __init__(self, size):
        self.__size = size
        self.integer_validator('size', self.size)

    def area(self):
        return (self.__size * 2)

    def __str__(self):
        return ("[Rectangle] {}/{}".format(self.__size, self.__size))
