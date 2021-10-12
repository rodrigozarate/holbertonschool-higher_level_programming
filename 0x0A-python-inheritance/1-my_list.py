#!/usr/bin/python3
""" Module list inheritance """


class MyList(list):
    """ Class MyList base for sorted """
    def print_sorted(self):
        """ Print given list sorted ascending """
        print(sorted(self))
