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
    for number in data:
        if (number >> 7) != 0:
            return False            
    return True
