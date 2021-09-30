#!/usr/bin/python3
""" Module Rectangle """


class Rectangle:
    """
        Rectangle Class

        Attribute:
            width (int): Private
            height (int): Private

    """
    def __init__(self, width=0, height=0):
        """
            Init Rectangle Class

            Args:
                width (int): width
                height (int): height
        """
        self.width = width
        self.height = height

    @property 
    def width(self):
        """
           width method get

           Return: width (int)
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
           width method set

        Args:
            Value (int): value
        Raises:
            TypeError: value not (int)
            ValueError: value < 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
           height method get
        Return: height (int)
        """
        return self._height

    @height.setter
    def height(self, value):
        """
           height method set
        Args:
            Value (int): value
        Raises:
            TypeError: value not (int)
            ValueError: value < 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value