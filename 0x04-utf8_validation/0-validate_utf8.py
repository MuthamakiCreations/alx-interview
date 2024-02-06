#!/usr/bin/python3
"""Determines a valid UTF-8 encoding"""


def validUTF8(data):
    """
    Checks if a list of integers (data) is valid UTF-8 encoding
    """

    bit1 = 1 << 7
    bit2 = 1 << 6
    byte_cnt = 0

    if not data or len(data) == 0:
        return True

    for symbol in data:
        bit = 1 << 7
        if byte_cnt == 0:
            while (bit & symbol):
                byte_cnt += 1
                bit = bit >> 1

            if byte_cnt == 0:
                continue
            if byte_cnt == 1 or byte_cnt > 4:
                return False
        else:

            if not (symbol & bit1 and not (symbol & bit2)):
                return False
        byte_cnt -= 1

    if byte_cnt:
        return False
    else:
        return True
