#!/usr/bin/python3
"""Base Class"""
import json


class Base:
    """1.Base Class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes the base class.

        Args:
            id (int) : The identity of the base class
        """
        if id is not None:
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

    @staticmethod
    def from_json_string(json_string):
        """
        that returns the list of the JSON string representation
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        function that returns an instance with all
        attributes already set
        """
        dinstance = cls(1, 1)
        if dinstance is not None:
            dinstance.update(**dictionary)
        return dinstance

    @classmethod
    def load_from_file(cls):
        """function that returns a list of instances"""
        filename = cls.__name__ + ".json"
        newlist = []
        with open(filename, 'r') as me:
            newlist = cls.from_json_string(me.read())
            for i, e in enumerate(newlist):
                newlist[i] = cls.create(**newlist[i])
        return newlist
