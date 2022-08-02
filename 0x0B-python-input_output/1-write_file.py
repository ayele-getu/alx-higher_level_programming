#!/usr/bin/python3
"""Defines a file-writing function"""


def write_file(filename = "", text = ""):
    """Writes astring to UTF8 texxt file"""

    with open(filename, mode = "w", encoding = "utf-8") as file_object:
        return file_object.write(text)
