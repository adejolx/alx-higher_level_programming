#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    arg_len = len(argv) - 1

    i = 1
    sum = 0
    while (i <= arg_len):
        sum += int(argv[i])
        i += 1

    print("{:d}".format(sum))
