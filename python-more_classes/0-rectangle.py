#!/usr/bin/python3
"""This module defines a rectangle by its width and height"""

class Rectangle:
    """A class that defines a rectangle by its width and height"""

    def __init__(self, width=0, height=0):
        """Initialize the rectangle with a given width and height."""
        self.width = width
        self.height = height

        @property
        def width(self):
            """Get the width of the rectangle."""
            return self.__width
        
        @width.setter
        def width(self, value):
            """Set the width of the rectangle with validation.
            
            Args:
                value(int): The width of the rectangle.
            Raises:
                Type Error: if width is not an integer.
                Value Error: if width is less than 0."""
            
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >=0")
            self._width = value

        @property
        def height(self):
            """Get the height of the rectcangle."""
            return self.__height
        
        @height.setter
        def height(self, value):
            """Set the height of the rectangle with validation.
            
            Args:
                value(int): The height of the rectangle.
            Raises:
                Type Error: if height is not an integer.
                Value Error: if height is less than 0."""
            
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            if value < 0:
                raise ValueError("height must be >=0")
            self._height = value
