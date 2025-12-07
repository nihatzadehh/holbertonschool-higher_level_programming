#!/usr/bin/python3
"""This is my doc"""

import requests
import sys

if __name__ == '__main__':
    try:
        data = {'q': sys.argv[1]}
    except IndexError:
        data = {'q': ''}
    url = 'http://0.0.0.0:5000/search_user'
    response = requests.post(url, data=data)
    try:
        data = response.json()
        if data:
            id = data.get('id')
            print(f'[{id}]', data['name'])
        else:
            print('No result')
    except requests.exceptions.RequestException:
        print('Not a valid JSON')
