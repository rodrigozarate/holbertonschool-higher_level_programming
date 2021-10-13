#!/usr/bin/python3
""" Module read file UTF8 """


def read_file(filename=""):
    """ read file implementation """
    with open(filename, "r", encoding="utf-8") as myfile:
        print(myfile.read(), end="")
