#!/usr/bin/python3
'''Document of the module'''


def read_file(filename=""):
    '''Document of func'''
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        print(f, end='')
