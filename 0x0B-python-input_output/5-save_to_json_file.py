#!/usr/bin/python3
"""Save Object to a file """
import json
"""json module to be used"""


def save_to_json_file(my_obj, filename):
    """
    function that writes an Object to a text file
    using a JSON representation
    """
    with open(filename, "w", encoding="utf-8") as e:
        data = json.dumps(my_obj)
        e.write(data)
