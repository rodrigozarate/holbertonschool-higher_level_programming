#!/usr/bin/python3
""" Module append file UTF8 """


def append_write(filename="", text=""):
    with open(filename, "a", encoding="utf-8") as myfile:
        myfile.write(text)
    return len(text)
