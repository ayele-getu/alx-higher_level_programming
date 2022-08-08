#!/usr/bin/python3
from models.base import Base
"""Importing the class called Base"""

class Rectangle(Base):
    """
    Representing a new class called Rectangle.
    It inherits all the attributes and methods from the class Base
    Base is the parent class and Rectangle is the child class
    """


    def __init__(self, width, height, x = 0, y = 0, id = None):
        """intitializing instances for the child class"""

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def width(self):
        """set the width of a rectangle"""
        return self._width

    def height(self):
        """set the height of a rectangle"""
        return self._height

    def x(self):
        """set the x-coordinate of a rectangle"""
        return self._x

    def y(self):
        """set the y-coordinate of a rectangle"""
        return self._y

    def width(self, value):
        """get the correct value of width of rectangle"""

        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif (value <= 0):
            raise ValueError('width must be >= 0')
        else:
            self._width = value

    def height(self, value):
        """get the correct value of height of rectangle"""

        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif (value < 0):
            raise ValueError('height must be >= 0')
        else:
            self._height = value

    def x(self, value):
        """get the correct value of x-coordinate of rectangle"""

        if type(value) is not int:
            raise TypeError('x must be an integer')
        elif (value < 0):
            raise ValueError('x must be >= 0')
        else:
            self._x = value

    def y(self, value):
        """get the correct value of y-coordinate of rectangle"""

        if type(value) is not int:
            raise TypeError('y must be an integer')
        elif (value <= 0):
            raise ValueError('y must be >= 0')
        else:
            self._y = value

    def area(self):
        """find the area of a rectangle"""
        return self.width * self.height

    def display(self):
        """print the rectangle using the # character """
        if (self.width == 0) or (self.height == 0):
            print()
            return

        [print() for y in range(0, self.y)]
        for h in range(0, self.height):
            [print(" ", end="") for x in range(0, self.x)]
            [print("#", end="") for w in range(0, self.width)]
            print()

    def __str__(self):
        """Return the print() and str() representation of the Rectangle."""
        return ('[Rectangle] ({}) {}/{} - {}/{}'.format(self.id, self.x,self.y, self.width,self.height))


