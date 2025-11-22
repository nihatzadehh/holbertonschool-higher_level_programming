#!/usr/bin/python3
def multiply_by_2(b_dictionary):
    c = b_dictionary.coppy()
    keys = list(c.keys())
    for i in keys:
        c[i] = c[i]*2
    return c
