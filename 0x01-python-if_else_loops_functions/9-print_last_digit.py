#!/usr/bin/python3

def getAbsoluteVal(n):
    return abs(n)


def getLastDigit(n):
    return getAbsoluteVal(n) % 10


def print_last_digit(number):
    print("{}".format(getLastDigit(number)), end="")
    return getLastDigit(number)
