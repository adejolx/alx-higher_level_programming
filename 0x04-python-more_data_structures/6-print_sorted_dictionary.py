#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    temp_list = sorted(list(a_dictionary.items()))

    for i in temp_list:
        print("{}: {}".format(i[0], i[1]))
