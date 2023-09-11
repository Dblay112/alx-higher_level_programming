#!/usr/bin/python3
"""6. Improve Geometry"""


class BaseGeometry:
    """Geometry module """
    def area(self):
        """function to calculate area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """function that validates value"""
        self.name = name
        self.value = value

        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
