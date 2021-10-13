#!/usr/bin/python3
""" Module represent pascal triangle """


def pascal_triangle(n):
    pascal = []
    if n <= 0:
        return pascal

    i = 1
    base = 1
    while i < n + 1:
        items = i + 1
        """ pascal formula """
        """ (x + y)^n """
        list = []
        coeficient = 1
        for x in range(1, items):
            list.append(coeficient)
            coeficient = coeficient * (i - x) // x

        pascal.append(list)
        i += 1
    return pascal
