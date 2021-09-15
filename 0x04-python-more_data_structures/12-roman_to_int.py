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
    valid_pair = ['I','X','C','M']
    if not roman_string or not isinstance(roman_string, str):
        return 0

    # at least is string and is not None
    sum = 0
    howmany = len(roman_string)

    if howmany == 1:
        # do simple replace
        if roman_string in romans_dic:
            return romans_dic[roman_string]
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
        if a > b:
            sum = a + b
        elif a == b:
            #Check that is in valid pair 1 10 100 1000
            if roman_string[0] in valid_pair:
                sum = a + b
            else:
                return 0
        else:
            # check for malformed pairs
            # substract
            sum = b - a

    if howmany > 2:
        # check that no more than 3 repetitions occur

        for x in range(len(roman_string)):
        # multiple checks
            # all except last char
            if x < len(roman_string) - 1:
                if romans_dic[roman_string[x]] < romans_dic[roman_string[x + 1]]:
                    # must substract 
                    # must verify is valid 
                    sum -= romans_dic[roman_string[x]]
                elif romans_dic[roman_string[x]] == romans_dic[roman_string[x + 1]]:
                    if roman_string[x] in  valid_pair:
                        # all fine add
                        sum += romans_dic[roman_string[x]]
                else:
                    sum += romans_dic[roman_string[x]]
        # last number
        sum += romans_dic[roman_string[x]]

    return sum
