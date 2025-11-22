#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        print(*my_list[:x], sep='')
        return x
    except:
        count = 0
        for i in my_list:
            print(i, end='')
            count += 1
        return count
