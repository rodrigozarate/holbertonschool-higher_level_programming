#!/usr/bin/python3
""" Module to find a peak in a list of integers """


def find_peak(list_of_integers):
    """ Get the peak by comparison in a list of integers """
    elements = len(list_of_integers)
    if list_of_integers == []:
        return None
    if elements == 1:
        return list_of_integers[0]
    if list_of_integers[0] >= list_of_integers[1]:
        return list_of_integers[0]
    if list_of_integers[elements - 1] >= list_of_integers[elements - 2]:
        return list_of_integers[elements - 1]
    for i in range(1, elements - 1):
        if list_of_integers[i] >= list_of_integers[i - 1] and \
           list_of_integers[i] >= list_of_integers[i + 1]:
            return list_of_integers[i]
