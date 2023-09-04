#!/usr/bin/python3
"""area and perimter"""


class Rectangle:
    """class that defines a rectangle"""
    def __init__(self, width=0, height=0):
        """
        Initializes a class rectangle with a given width and height
        
        Args:
        width (optional, int): the width of the rectangle. Default equals 0
        height (optional, int): the height of the rectangle. Default equals 0
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        gets width of the rectangle
        """
        self.__width

    @width.setter
    def width(self, value):
        """
        sets the width of the rectangle

        Args:
        value (int): new width of the rectangle

        Raises:
        TypeError: if value is not an integer
        ValueError: if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        gets the height of a rectangle

        Returns:
        int: height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        sets the height of the rectangle

        Args:
        value (int): new height of the rectangle

        Raises:
        TypeError: if height is not an integer
        ValueError: if height is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return the perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
