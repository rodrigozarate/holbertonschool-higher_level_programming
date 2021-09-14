#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_list = []
    for x in my_list:
        if x not in unique_list:
            unique_list.append(x)

    total = 0
    for val in unique_list:
        total += val

    return total
