#!/usr/bin/python3
"""A script that determines if a given dataset
    represents a valid UTF-8 encoding
"""


def validUTF8(data):
    """Return True if all data elements are valid utf-8 strings

    Args:
        data (list): List of numbers(bytes)

    Returns:
        Boolean denoting if all are valid utf-8 encodings
    """
    num_bytes = 0
    for num in data:
        if num_bytes == 0:
            if num & 0xf0 == 0x80:
                return False
            elif num & 0xf8 == 0xf0:
                num_bytes = 4
            elif num & 0xf0 == 0xe0:
                num_bytes = 3
            elif num & 0xf0 == 0xc0:
                num_bytes = 2
            else:
                num_bytes = 1
        else:
            if num & 0xf0 != 0x80:
                return False
        num_bytes -= 1
    return num_bytes == 0
