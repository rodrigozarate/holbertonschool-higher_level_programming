#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if not my_list:
        return "None"

    for i in my_list.reverse():
        print ("{:d}".format(i))
