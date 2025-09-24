#!/usr/bin/python3
"""This module defines a Square class with a private instance attribute."""

class Square:
    """A class that defines a square by its size."""

    def __init__(self, size):
        """Initialize the square with a given size.

        Args:
            size (int): The size of the square's sides.
        """
        self.__size = size
