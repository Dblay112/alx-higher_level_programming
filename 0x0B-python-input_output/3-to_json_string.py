#!/usr/bin/python3
"""3. To JSON string """
import json
"""module to use json"""


def to_json_string(my_obj):
    """function that returns the JSON representation of an objec"""

    return json.dumps(my_obj)
