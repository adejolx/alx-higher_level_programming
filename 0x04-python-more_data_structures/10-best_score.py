#!/usr/bin/python3

def best_score(a_dictionary):
    h_val = 0
    h_key = ""

    if a_dictionary:
        for key, val in a_dictionary.items():
            if a_dictionary[key] > h_val:
                h_val = val
                h_key = key
    else:
        h_key = None

    return h_key
