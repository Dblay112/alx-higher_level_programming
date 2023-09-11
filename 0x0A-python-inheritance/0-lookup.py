#!/usr/bin/python3
"""0.Lookup"""


def lookup(obj):
    """
    function to return the list of available attributes

    Args:
    obj : object to get the methods and attributes for

    Return:
    list of strings containing name of attribute
    """
    attributes = []
    methods = []

    for name in dir(obj):
        if name.startswith("__") and name.endswith("__"):
            continue
        if callable(getattr(obj, name)):
            methods.append(name)
        else:
            attributes.append(name)

    return methods + attributes
