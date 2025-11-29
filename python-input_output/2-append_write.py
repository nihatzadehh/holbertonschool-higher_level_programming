#!/usr/bin/python3
"""Just a documentation"""


def append_write(filename="", text=""):
    """My documentation only"""
    with open(filename, 'a') as f:
        f.write(text)
    return len(text)
