#!/usr/bin/python3
"""Load, add, save """
from sys import argv
from os import path

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file


def main():
    """main code in function
    """
    filename = "add_item.json"
    if path.isfile(filename):
        arg_list = load_from_json_file(filename)
    else:
        arg_list = []
    for i in range(1, len(argv)):
        arg_list.append(argv[i])
    save_to_json_file(arg_list, filename)


main()