#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    infinite_add = 0
    for element in sys.argv[1:]:
        infinite_add += int(element)
    print("{:d}".format(infinite_add))
