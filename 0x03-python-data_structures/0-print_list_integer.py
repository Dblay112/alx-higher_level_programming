#!/usr/bin/python3
def print_list_integer(my_list=[]):
    
    for number in my_list:
        print(f"{number:d}".format(my_list), end="\n")
