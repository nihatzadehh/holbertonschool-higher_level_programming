#!/usr/bin/python3
"""This is my doc"""


import requests
import sys

if __name__ == '__main__':
    try:
        data = {'q': sys.argv[1]}
    except:
        data = {'q': ''}
    response = requests.post('http://0.0.0.0:5000/search_user', data=data)
    response = response.text
    if response is None:
        print('Not a valid JSON')
    elif len(response) == 0:
        print('No result')
    else:
        print(response.text)
