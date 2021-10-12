#!/usr/bin/python3
""" Module list inheritance """


class MyList(list):
    """ Class MyList """
    def print_sorted(self):
        """ Print given list sorted ascending """
        print(sorted(self))
