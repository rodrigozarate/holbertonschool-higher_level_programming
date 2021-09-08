#!/usr/bin/python3
def uppercase(str):

    modified_str = ""
    for i in str:
        ascii = ord(i)

        if (ascii >= ord('a') and
           ascii <= ord('z')):
            modified_str += chr(ascii - 32)
        else:
            modified_str += i

    print(modified_str, end="")
