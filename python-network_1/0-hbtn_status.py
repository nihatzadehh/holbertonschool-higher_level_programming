#!/usr/bin/python3
"""This is my doc"""


import urllib.request


url = 'https://intranet.hbtn.io/status'
with urllib.request.urlopen(url) as response:
    data = response.read()
    dt = type(data)
    utfcont = data.decode('utf-8')
    print('Body response:$')
    print('\t- type: {}\n\t- content: {}\n\t- utf8 content: {}'.format(dt,data, utfcont))
