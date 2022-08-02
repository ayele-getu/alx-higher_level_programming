#!/usr/bin/python3
"""writing a text to a file"""


def write_file(filename = "", text = ""):
    """write a text file to utf8"""

    with open(filename, mode = "w", encoding = "utf-8") as file_object:
        return file_object.write(text)
