#!/usr/bin/python3
""" Module write file UTF8 """


def write_file(filename="", text=""):
    with open(filename, "w", encoding="utf-8") as myfile:
        myfile.write(text)
    return len(text)
