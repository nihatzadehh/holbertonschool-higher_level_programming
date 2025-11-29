#!/usr/bin/python3
"""Just
a doccument"""


class Student:
    """This is my doccumentation"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if not attrs:
            return self.__dict__
        elif len(attrs) == 0:
            return '{}'
        else:
            dictwillreturn = {}
            for i in attrs:
                if self.__dict__.get(i):
                    dictwillreturn[i] = self.__dict__.get(i)
            return dictwillreturn
