#!/usr/bin/python3
"""Student to JSON """


class Student:
    """class that defines a student"""

    def __init__(self, first_name, last_name, age):
        """Initializing of the class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


    def to_json(self):
        """retrieving a dictinary representation"""
        return {
                "first_name": self.first_name,
                "last_name": self.last_name,
                "age": self.age,
                }
