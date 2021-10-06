#!/usr/bin/python3
"""
Module Add Integer
"""


def add_integer(a, b=98):
    """
    Add integer a, b
    """
    if not isinstance(a, int):
        raise TypeError('a must be integer')
    if not isinstance(b, int):
        raise TypeError('b must be integer')
    return a + b
