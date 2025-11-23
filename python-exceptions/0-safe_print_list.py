#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        if my_list[x-1]:
            print(*my_list[:x], sep='')
            return x
    except:
        counter = 0
        for i in my_list:
            print(i, end='')
            counter += 1
        return counter
