#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    how_many_args = len(sys.argv[1:])

    if how_many_args == 0:
        header = "arguments."
    elif how_many_args == 1:
        header = "argument:"
    elif how_many_args > 1:
        header = "arguments:"
    print("{:d} {}".format(how_many_args, header))

    i = 1
    for arg in sys.argv[1:]:
        print("{:d}: {}".format(i, arg))
        i += 1
