#!/usr/bin/python3

def pow(a, b):
    powerProduct = 1
    if (b == 0):
        return 1

    elif (b > 0):
        for i in range(b):
            powerProduct = powerProduct * a

    elif (b < 0):
        for i in range(b, 0):
            powerProduct = powerProduct * a
        powerProduct = 1 / powerProduct

    return powerProduct
