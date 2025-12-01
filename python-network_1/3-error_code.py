#!/usr/bin/python3
"""This is just a doc"""


import urllib.request
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    with urllib.request.urlopen(url) as r:
        try:
            print(r.read())
        except:
            print(f'Error code: {r.satus}')
