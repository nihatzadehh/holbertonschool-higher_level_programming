#!/usr/bin/python3
"""This is my doccumentation"""


import sys
import urllib.request


url = sys.argv[1]
with urllib.request.urlopen(url) as response:
    header = response.getheader('X-Request-Id')
    print(header)
