#!/usr/bin/python3
def multiple_returns(sentence):
    howlong = len(sentence)
    if howlong > 0:
        return(howlong, sentence[0])
    else:
        return(howlong, None)
