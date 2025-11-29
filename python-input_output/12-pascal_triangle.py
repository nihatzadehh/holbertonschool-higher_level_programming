#!/usr/bin/python3
"""This is just a doc"""


def pascal_triangle(n):
    """This is just a doc"""
    result = []
    for i in range(1, n+1):
        thisstage = []
        for j in range(1, i+1):
            if j == 1 or j == i:
                thisstage.append(1)
            else:
                thisstage.append(result[i-2][j-1] + result[i-2][j-2])
        result.append(thisstage)
    return result
