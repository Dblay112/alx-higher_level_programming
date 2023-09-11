#!/usr/bin/python3
"""8. Rectangle"""


class Rectangle(BaseGeometry):
    """function that that inherits from BaseGeometry"""
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
