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
        num = num & 0xff
        if num_bytes == 0:
            if num & 0x80 == 0x00:
                continue
            elif num & 0xf8 == 0xf0:
                num_bytes = 4
            elif num & 0xf0 == 0xe0:
                num_bytes = 3
            elif num & 0xe0 == 0xc0:
                num_bytes = 2
            else:
                return False
        else:
            if (num & 0xc0) != 0x80:
                return False
        num_bytes -= 1
    return num_bytes == 0
