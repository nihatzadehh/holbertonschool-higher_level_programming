"""This
is my docummentation
"""
#!/usr/bin/python3



import json, sys

def load_from_json_file(filename):
    """Just a doc 2"""

    with open(filename, "r") as f:
        data = f.read()
        if not data:
            return []
        return json.loads(data)
        f.close()


def save_to_json_file(my_obj, filename):

    '''Just a doc'''

    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))

file = open('add_item.json', 'a')
file.close()
currentdata = load_from_json_file('add_item.json')

if len(sys.argv) > 1:
    finaldata = currentdata + sys.argv[1:]
    save_to_json_file(finaldata, 'add_item.json')
else:
    save_to_json_file(currentdata, 'add_item.json')
