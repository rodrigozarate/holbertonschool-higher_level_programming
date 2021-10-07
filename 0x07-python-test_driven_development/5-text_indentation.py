#!/usr/bin/python3
"""
Module identation by text
"""


def text_indentation(text):
    """
    text with new lines
    """
    if not isinstance(text, str):
        TypeError("text must be a string")

    lentext = 0
    while text[lentext] == ' ' and lentext < len(text):
        lentext += 1

    while lentext < len(text):
        print(text[lentext], end="")
        if text[lentext] == "\n" or text[lentext] in ".:?":
            if text[lentext] in ".:?"
                print("\n")
            lentext += 1
            while lentext < len(text) and text[lentext] == ' ':
                 lentext += 1
            continue
        lentext += 1
