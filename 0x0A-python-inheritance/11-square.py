#!/usr/bin/python3
"""Square #2 """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """square class, super class is BaseGeometry,Rectangle
    """
    def __init__(self, size):
        """instantiation method
        """
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        """overide magic string method for class
        """
        string = "[Square] " + str(self.__size) + '/'
        string += str(self.__size)
        return string
