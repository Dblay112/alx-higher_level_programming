#!/usr/bin/python3
"""Load, add, save"""

import json
import sys


def save_to_json_file(my_obj, filename):
    """
    function that writes an Object to a text file
    using a JSON representation
    """
    with open(filename, "w", encoding="utf-8") as e:
        data = json.dumps(my_obj)
        e.write(data)


def load_from_json_file(filename):
    """function that creates an Object from a “JSON file
    """
    with open(filename, "r", encoding="utf-8") as e:
        return json.load(e)


def main():
    """main function to get arguments"""
    arg_count = sys.argv[1:]
    arg_list = []

    for i in arg_count:
        arg_list.append(i)

    save_to_json_file(arg_list, "add_item.json")
