#!/usr/bin/python3
"""Base Class"""


class Base:
    """1.Base Class"""

    __n_objects = 0

    def __init__(self, id=None):
        if id is None:
            self.id = id
        else:
            Base.__nb_objects = + 1
            self.Base.__nb_objects += 1
