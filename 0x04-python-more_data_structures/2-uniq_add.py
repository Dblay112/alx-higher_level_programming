#!/usr/bin/python3

def uniq_add(my_list=[]):

    uniq_integers = set()
    sum_of_ui = 0

    for i in my_list:
        if i not in uniq_integers:
            uniq_integers.add(i)
            sum_of_ui += i

    return sum_of_ui
