#!/usr/bin/python3
    """task 6
    """
import json
    """module to be used
    """
def load_from_json_file(filename):
    """function that creates an Object from a “JSON file
    """
    with open(filename, "r", encoding="utf-8") as e:
        return json.load(e)
