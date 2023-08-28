#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):

    e_count = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]))
            e_count += 1
        except TypeError:
            pass
    print()
    return e_count
