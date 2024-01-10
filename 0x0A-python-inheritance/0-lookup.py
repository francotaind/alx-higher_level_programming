#!/usr/bin/python3
    """Defines function that returns list attr"""
def lookup(obj):
    """
    Get list of available attributes and methods of an object
    Parameters: 
    -obj: The object to inspect
    Returns:
    -A list containing names of attr and methods
    """
    return(dir(obj))
