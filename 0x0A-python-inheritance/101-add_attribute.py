#!/usr/bin/python3
"""Can I """


def add_attribute(a_class, att_name, att_value):
    """
    function that adds a new attribute to an object if it’s possible
    """
    if not hasattr(a_class, "__dict__"):
        raise TypeError("can't add new attribute")
    else:
        setattr(a_class, att_name, att_value)
