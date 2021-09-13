#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a_length = len(tuple_a)
    tuple_b_length = len(tuple_b)

    if tuple_a_length == 0:
        tozero1a = 0
        tozero2a = 0
    
    if tuple_b_length == 0:
        tozero1b = 0
        tozero2b = 0

    if tuple_a_length == 1:
        tozero1a = tuple_a[0]
        tozero2a = 0
    
    if tuple_b_length == 1:
        tozero1b = tuple_a[0]
        tozero2b = 0

    if tuple_a_length >= 2:
        tozero1a = tuple_a[0]
        tozero2a = tuple_a[1]

    if tuple_b_length >= 2:
        tozero1b = tuple_b[0]
        tozero2b = tuple_b[1]

    one = tozero1a + tozero1b
    two = tozero2a + tozero2b

    return(one, two)
