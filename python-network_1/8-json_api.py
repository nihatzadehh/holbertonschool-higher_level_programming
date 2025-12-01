#!/usr/bin/python3
"""This is my doc"""

import requests
import sys

if __name__ == '__main__':
    try:
        # Attempt to get query parameter from command line arguments
        data = {'q': sys.argv[1]}
    except IndexError:
        # If no argument is passed, set the default value for 'q'
        data = {'q': ''}

    # Send POST request to the server with the query parameter 'q'
    response = requests.post('http://0.0.0.0:5000/search_user', data=data)

    # Check if the response was successful and handle various cases
    try:
        # Try to parse the response as JSON
        response_json = response.json()
    except ValueError:
        # If the response isn't valid JSON
        print('Not a valid JSON')
    else:
        # If the response is valid JSON, handle it accordingly
        if not response_json:
            print('No result')
        else:
            print(response_json)

