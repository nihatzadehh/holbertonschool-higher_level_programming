#!/usr/bin/python3
"""This is my doc"""


class Rectangle():
    """This is mine also"""

    def __init__(self, width=0, height=0):
        if isinstance(width, int):
            if width > 0:
                self.width(width)
            else:
                raise ValueError('width must be >= 0')
        else:
            raise TypeError('width must be an integer')
        if isinstance(height, int):
            if height > 0:
                self.height(height)
            else:
                raise ValueError('height must be >= 0')
        else:
            raise TypeError('height must be an integer')
    def width(self, value):
        self._Rectangle__width = value
    
    def height(self, value):
        self._Rectangle__height = value
