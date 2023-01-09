#!/usr/bin/python3
def getAsciiVal(c):
    return ord(c)


def subtract32(n):
    return n - 32


def getCharVal(n):
    return chr(n)


def uppercase(str):
    for i in range(0, len(str) + 1):
        if (i == len(str)):
            print("")
            break
        print("{}".format(getCharVal(subtract32(getAsciiVal(str[i]))))
              if getAsciiVal(str[i]) >= 97
              and getAsciiVal(str[i]) < 123 else str[i], end="")
