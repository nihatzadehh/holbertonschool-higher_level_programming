#!/usr/bin/python3
'''Document of the module'''


def write_file(filename="", text=""):
    '''Document of func'''
    with open(filename, 'wa', encoding='utf-8') as f:
        f.write(text)
        return len(text)
