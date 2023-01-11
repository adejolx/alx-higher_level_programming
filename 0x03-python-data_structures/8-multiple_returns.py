#!/usr/bin/python3

def get_length(string):
    return len(string)


def get_first_char(string):
    return string[0]


def multiple_returns(sentence):
    if (not sentence):
        return None

    str_length = get_length(sentence)
    first_char = get_first_char(sentence)

    new_tuple = str_length, first_char

    return new_tuple
