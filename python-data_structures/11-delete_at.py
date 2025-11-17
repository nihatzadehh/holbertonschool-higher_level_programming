#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    newlist = list()
    if idx >= 0 and idx < len(my_list):
        for i in range(len(my_list)):
            if i != idx:
                newlist.append(my_list[i])
        return newlist
    else:
        return my_list
