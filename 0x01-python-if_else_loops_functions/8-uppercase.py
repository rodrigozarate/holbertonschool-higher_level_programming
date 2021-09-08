#!/usr/bin/python3
def uppercase(str):

    for i in str:
        ascii = ord(i)

        if (ascii >= ord('a') and
           ascii <= ord('z')):
            print("{:c}".format(ascii - 32), end="")
        else:
            print("{:s}".format(i), end="")
    print("")
