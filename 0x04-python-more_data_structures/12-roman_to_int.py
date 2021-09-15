#!/usr/bin/python3
def roman_to_int(roman_string):
    """the meaning of I change if its placed after or before another number
       consecutive I is to be added or subtracted accordingly. 
       Every letter have special meaning:
       I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, M = 1000.
       Addition goes till 3 but substraction only to 1
       but number can be compound so IVX does not work
       a dictionary can get the list of possible numbers
       rule goes like this if next is equal add
       if next is mayor substract from next
       but I can not be substracted from C to form 99
       99 must be constructed XCIX"""

    romans_dic = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

    sum = 0
    howmany = len(roman_string)

    if howmany == 0:
        # no string
        return 0
    if howmany == 1:
        # do simple replace
        if i in romans_dic:
            print(romans_dic[i])
            return romans_dic[i]
        else:
            # malformed number
            return 0

    if howmany == 2:
        # check for valid pairs

        # sum
        if roman_string[0] in romans_dic:
            a = romans_dic[roman_string[0]]
        else:
            return 0
            # malformed number

        if roman_string[1] in romans_dic:
            b = romans_dic[roman_string[1]]
        else:
            return 0
            # malformed number

        # both numbers exists at this point
        if a >= b:
            sum = a + b
            print(sum)
        else:
            # check for malformed pairs
            # substract
            sum = b - a
            print(sum)

    if howmany > 2:
        # check that no more than 3 repetitions occur
        print(howmany)

        for a in range(len(roman_string)):
        # multiple checks
            sum += romans_dic[roman_string[a]]

        for key in romans_dic:
            print("{}: {}".format(key, romans_dic[key]))
    
    print(sum)
    return sum

i = 'LL'
roman_to_int(i) 
