#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    arg_len = len(argv) - 1

    if (len(argv) < 2):
        print("{:d} arguments.".format(arg_len))
    elif (len(argv) == 2):
        print("{:d} argument:".format(arg_len))
    elif (len(argv) > 2):
        print("{:d} arguments:".format(arg_len))

    i = 1
    while (i <= arg_len):
        print("{:d}: {}".format(i, argv[i]))
        i += 1
