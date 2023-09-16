#!/usr/bin/python3
"""module  defining square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class defining square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """string representation of square"""
        s = "[Square] ({:d}) {:d}/{:d} - {:d}"
        return s.format(self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        if args is not None and len(args) > 0:
            for i in args:
                if i == 0:
                    self.id = i
                if i == 1:
                    self.size = i
                if i == 2:
                    self.x = i
                if i == 3:
                    self.y = i
        elif kwargs is not None:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """return a dictionary"""
        return {
                'id' = self.id,
                'size' = self.size,
                'x' = self.x,
                'y' = self.y
                }
