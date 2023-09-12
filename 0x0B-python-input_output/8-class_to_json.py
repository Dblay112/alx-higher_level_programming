#!/usr/bin/python3
"""8. Class to JSON"""


def class_to_json(obj):
    """
    function that returns the dictionary
    description with simple data structure
    """
    json_dict = {}
    for key, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            json_dict[key] = value
        elif isinstance(value, (tuple, set)):
            json_dict[key] = list(value)

    return json_dict
