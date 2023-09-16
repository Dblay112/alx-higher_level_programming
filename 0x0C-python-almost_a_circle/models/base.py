#!/usr/bin/python3
"""Base Class"""


class Base:
    """1.Base Class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes the base class.

        Args:
            id (int) : The identity of the base class
        """
        if id is None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
