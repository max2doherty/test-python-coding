#!/usr/bin/python3
"""This modules defines a Square class with a private instance attribute and
validates the size attribute to ensure it is a non-negative integer."""


class Square:
    """A class that defines a square by its size."""

    def __init__(self, size=0):
        """Initialize the square with a given size.

        Args:
            size (int): The size of the square's sides. Default is 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
