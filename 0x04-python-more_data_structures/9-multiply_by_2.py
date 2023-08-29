#!/usr/bin/python3

def multiply_by_2(a_dictionary):

    new_dic = {}
    for key, val in a_dictionary.items():
        new_val = val * 2
        new_dic[key] = new_val

    return new_dic
