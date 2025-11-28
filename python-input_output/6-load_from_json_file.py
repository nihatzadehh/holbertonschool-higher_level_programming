#!/usr/bin/python3
"""Just a doc"""

import json


def load_from_json_file(filename):
    """Just a doc 2"""

    with open(filename, "r") as f:
        data = f.read()
        return json.loads(data)
        f.close()
