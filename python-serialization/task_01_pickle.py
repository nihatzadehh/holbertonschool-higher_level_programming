#!/usr/bin/python3
"""Just a documentation"""


import pickle


class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student
    def display(self):
        print('Name: {}'.format(self.name))
        print('Age: {}'.format(self.age))
        print('Is Student: {}'.format(self.is_student))
    def serialize(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self.__dict__, f)
    @classmethod
    def deserialize(cls, filename):
        with open(filename, 'rb') as f:
            data = f.read()
            return CustomObject(pickle.loads(data)['name'], pickle.loads(data)['age'], pickle.loads(data)['is_student'])
