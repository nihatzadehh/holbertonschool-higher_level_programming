#!/usr/bin/python3
"""This is my doc"""


import requests
import sys


url = sys.argv[1]
respond = requests.get(url)
print(respond.headers.get('X-Request-Id'))
