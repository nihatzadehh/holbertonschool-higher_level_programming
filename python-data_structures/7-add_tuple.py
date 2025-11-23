#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    def get_first_two(tup):
        padded_tuple = tup + (0, 0)
        return padded_tuple[0], padded_tuple[1]

    a1, a2 = get_first_two(tuple_a)
    b1, b2 = get_first_two(tuple_b)

    first_element_sum = a1 + b1
    second_element_sum = a2 + b2

    return (first_element_sum, second_element_sum)
