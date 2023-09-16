#!/usr/bin/python3
"""First Rectangle"""
from models.base import Base


class Rectangle(Base):
    """
    class decribing Rectang;e
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes the class Rectangle

        Args:
        width: width of the rectangle
        height: height of the rectangle
        x: x co-ordinate
        y: y co-ordinate

        Raises:
        TypeError: If either of width or height is not an int.
        ValueError: If either of width or height <= 0.
        TypeError: If either of x or y is not an int.
        ValueError: If either of x or y < 0
        """

        self.width = width
        self.height
        self.x = x
        self.y = y

        super().__init__(id)

    @property
    def width(self):
        """sets/gets the value of the rectang;e"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("value must be an integer")
        if value < 0:
            raise ValueError("value must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get/set the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def x(self):
        """set/get the x co-ordinate of the rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """set/get the y co-ordinate of the retangle"""
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """area of the rectangle"""
        return self.width * self.height

    def display(self):
        """print # to stdout"""
        for line in range(0, self.y):
            print()
        for i in range(0, self.height):
            hashs = ""
            for curve in range(0, self.x):
                hashs += " "
            for j in range(0, self.width):
                hashs += "#"
            print(hashs)

    def __str___(self):
        """string representation of rectangle"""
        s = "[Rectangle] ({}) {}/{} - {}/{}"
        s.format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """positional argument"""
        if args is not None and len(args) > 0:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                if i == 1:
                    self.width = arg
                if i == 2:
                    self.height = arg
                if i == 3:
                    self.x = arg
                if i == 4:
                    self.y = arg
        elif kwargs is not None:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.width = value
                if key == "height":
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value
