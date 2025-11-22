#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    key = []
    for i in set_1:
        if i in set_2:
            pass
        else:
            key.append(i)
    for i in set_2:
        if i in set_1:
            pass
        else:
            key.append(i)
    return key
