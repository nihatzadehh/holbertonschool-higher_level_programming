#!/usr/bin/python3
"""This is my doc"""


import requests
import sys

if __name__ == '__main__':
    try:
        data = {'q': sys.argv[1]}
    except IndexError:
        data = {'q': ''}
    response = requests.post('http://0.0.0.0:5000/search_user', data=data)
    try:
	    responsejs = response.json()
        if not responsejs:
            print('No result')
        else:
            print(response.text)
    except ValueError:
        print('Not a valid JSON')

