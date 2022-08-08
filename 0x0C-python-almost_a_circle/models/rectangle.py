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
        """get the width of a rectangle"""
        return self._width

    def height(self):
        """get the height of a rectangle"""
        return self._height

    def x(self):
        """get the x-coordinate of a rectangle"""
        return self._x

    def y(self):
        """get the y-coordinate of a rectangle"""
        return self._y


