#!/usr/bin/python3

"""
A class of a square initializing a private instance
"""

class Square:
    """
    __size (int): THe size of a square which is a private attribute
    """
    def __init__(self, size):
    """
    The constructor for the square class.
    Args:
        size(int): The size of the square
    """
        self.__size = size
