#!/usr/bin/python3
def divisible_by_2(my_list=[]):
        newlist = []
        i = 0
        while i < len(my_list):
            if my_list[i] % 2 == 0:
                newlist.append(True)
            else:
                newlist.append(False)
            i += 1

        return newlist
