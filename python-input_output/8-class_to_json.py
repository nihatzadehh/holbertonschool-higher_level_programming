#!/usr/bin/python3
"""This
is my doc"""
import json

def class_to_json(obj):
    """This is my func's docum"""
    ourstr = json.dumps(obj.__dict__)
    return json.loads(ourstr)
