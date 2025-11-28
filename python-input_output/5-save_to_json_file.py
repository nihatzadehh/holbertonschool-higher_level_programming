#!/usr/bin/python3
'''Just a doc'''


import json

def save_to_json_file(my_obj, filename):
    
    '''Just a doc'''

    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
