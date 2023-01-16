#!/usr/bin/python3

def roman_to_int(roman_string):
    nums = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    str_len = len(roman_string)
    val_sum = 0

    if (not isinstance(roman_string, str) and roman_string is None):
        return 0

    for i in range(str_len):
        if i + 1 < str_len and nums[roman_string[i]] < nums[roman_string[i + 1]]:
                val_sum -= nums[roman_string[i]]
        else:
            val_sum += nums[roman_string[i]]
    return val_sum
