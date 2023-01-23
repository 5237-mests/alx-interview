#!/usr/bin/python3
""" Task for module 1
"""


def validUTF8(data):
    """return true if fine utf-8"""
    for i in data:
        if i > 255:
            return False
    return True
