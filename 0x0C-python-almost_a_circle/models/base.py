#!/usr/bin/python3
"""Base Class"""
import json
import turtle


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        func that  returns the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        function that that writes the JSON string
        representation of list_objs to a file:
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as me:
            if list_objs is None:
                me.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                me.write(Base.to_json_string(list_dicts))
