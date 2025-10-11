#!/usr/bin/python3
"""This module returns True if the object is exactly an instance
of the specified class ; otherwise False."""


def is_same_class(obj, a_class):
    """Check if the object is exactly an instance of the specified class.

    Args:
        obj: The object to check.
        a_class: The class to match the type of obj to.
    Returns:
        True if obj is exactly an instance of a_class, otherwise False.
    """
    return type(obj) is a_class
