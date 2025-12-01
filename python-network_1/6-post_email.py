#!/usr/bin/python3
"""This is my doc"""


if __name__ == '__main__':
    import sys
    import requests

    respond = requests.get(sys.argv[1], sys.argv[2])
    print(respond.text)
