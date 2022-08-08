#!/usr/bin/python3
"""Import the parent class called rectangle"""
from model.rectangle import Rectangle

class Square(Rectangle):
    """child class, Square inherits methods and attributes from Rectangle"""


    def __init__(self):
        """Initialize the class with __init__ function"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return ('[Square] ({}) {}/{} - {}'.format(self.id, self.x, self.y, self.width))

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """updates multiple attributes"""
        if len(args):
            for i, a in enumerate(args):
                if i == 0:
                    self.id = a
                elif i == 1:
                    self.size = a
                elif i == 2:
                    self.x = a
                elif i == 3:
                    self.y = a
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.width = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """Return the dictionary representation of the Square."""
        return ({"id": self.id, "size": self.width, "x": self.x, "y": self.y})
