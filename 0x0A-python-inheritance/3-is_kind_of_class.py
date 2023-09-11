#!/usr/bin/python3
"""3. Same class or inherit from"""


def is_kind_of_class(obj, a_class):
    """
    Checks if the object is an instance

    Args:
    obj :object to be checked
    a_class: class to compare against

    Return:
    True: if the object is an instance of, or if the object is an instance of a class that inherited from
    False: if otherwise
    """
    return isinstance(obj, a_class)
