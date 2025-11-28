#!/usr/bin/python3
''' Just a documentation '''


class Rectangle:
    ''' Just a documentation '''
    def __init__(self, width, height):
        self.width(width)
        self.height(height)


    def width(self, value):
        if isinstance(value, int):
            if value >= 0:
                self.__width = value
            else:
                raise ValueError('width must be >= 0')
        else:
            raise TypeError('width must be an integer')
    def height(self, value):
        if isinstance(value, int):
            if value >= 0:
                self.__height = value
            else:
                raise ValueError('height must be >= 0')
        else:
            raise TypeError('height must be an integer')
