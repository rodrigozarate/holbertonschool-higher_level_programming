#!/usr/bin/python3
"""
Module to print square
"""


def print_square(size):
    """
    Print a square based on the size
    """
    if size < 0:
        raise ValueError("size must be >= 0")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    for i in range(size):
        print("#" * size)
