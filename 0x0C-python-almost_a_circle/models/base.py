#!/usr/bin/python3
"""Define a Base class"""
class Base():
    """ An attempt to create a parent class called Base"""


    _nb_objects = 0

    def __init__(self, id = None):
        """Initializes id number to None """

        if id is not None:
            self.id = id
        else:
            Base._nb_objects += 1
            self.id = Base._nb_objects
