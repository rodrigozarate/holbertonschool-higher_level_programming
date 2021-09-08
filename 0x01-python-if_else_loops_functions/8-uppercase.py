#!/usr/bin/python3
def uppercase(str):

    for i in str:
        ascii = ord(i)

        print("{:c}".format(ascii - 32 if ascii >= 97 
             and ascii <= 122 else ascii), end="")
    print("")
