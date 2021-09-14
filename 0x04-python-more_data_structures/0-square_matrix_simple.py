#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = list(map(list, matrix))

    for newrow in new_matrix:
        i = 0
        for element in newrow:
            newrow[i] = element * element
            i += 1

    return new_matrix
