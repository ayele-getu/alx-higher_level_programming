#!/usr/bin/python3
""" A function ppending a text to a file"""


def append_write(filename="", text="") as file_oblject:
    """Appending a text to UTF8 file"""

    with open(filename, mode="a", encoding="utf-8"):
        file_object.append(text)
