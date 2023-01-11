#!/usr/bin/python3

def get_length(string):
    return len(string)


def get_first_char(string):
    if (not string):
        return None
    return string[0]


def multiple_returns(sentence):
    str_length = get_length(sentence)
    first_char = get_first_char(sentence)

    new_tuple = str_length, first_char

    return new_tuple
