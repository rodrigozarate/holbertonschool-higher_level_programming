#!/usr/bin/python3
def multiple_returns(sentence):
    howlong = len(sentence)
    if howlong > 1:
        first = sentence[0]
    else:
        first = "None"

    return(howlong, first)
