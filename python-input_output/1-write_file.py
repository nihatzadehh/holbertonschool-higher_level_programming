#!/usr/bin/python3
'''This code add text to file'''


def write_file(file, text):
    '''Practice with open function'''

    with open(file, 'w') as f:

        f.write(text)

    return len(text)
