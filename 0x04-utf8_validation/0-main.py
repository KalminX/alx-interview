#!/usr/bin/python3
"""
Main file for testing
"""

validUTF8 = __import__('0-validate_utf8').validUTF8

# Test case: Single ASCII character
data = [65]  # Expected output: True
print(validUTF8(data))

# Test case: Valid ASCII string
data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32,
        99, 111, 111, 108, 33]  # Expected output: True
print(validUTF8(data))

# Test case: Invalid byte with value > 255
data = [229, 65, 127, 256]  # Expected output: False
print(validUTF8(data))

# Test case: Valid 4-byte UTF-8 character
data = [240, 188, 128, 167]  # Expected output: True
print(validUTF8(data))

# Test case: Invalid bytes, out of UTF-8 range
data = [467, 133, 108]  # Expected output: False
print(validUTF8(data))

# Test case: Valid 4-byte UTF-8 character (repeated)
data = [240, 188, 128, 167]  # Expected output: True
print(validUTF8(data))
