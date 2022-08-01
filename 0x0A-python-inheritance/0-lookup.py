#!/usr/bin/bash/python3
"""Defines an object attribute lookup function"""

def lookup(obj):
    """Return alist of object's attribute"""
    return (dir(obj))
