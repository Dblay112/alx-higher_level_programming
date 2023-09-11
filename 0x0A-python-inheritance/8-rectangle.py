#!/usr/bin/python3
"""8. Rectangle"""


class BaseGeometry:
    """Geometry module """
    def area(self):
        """function to calculate area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """function that validates value"""

        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")


class Rectangle(BaseGeometry):
    """function that that inherits from BaseGeometry"""
    def __init__(self, width, height):
        super().__init__()
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
