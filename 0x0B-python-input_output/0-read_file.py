#!/usr/bin/python3
"""Reading a file in python"""

def read_file(filename = ""):
    """This function reads the text file called UTF8"""
    with open('UTF8.txt', r) as file_object:
        print(file_object.read())

