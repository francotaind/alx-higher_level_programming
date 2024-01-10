def lookup(obj):
    """
    Get list of available attributes and methods of an object
    Parameters: 
    -obj: The object to inspect
    Returns:
    -A list containing names of attr and methods
    """
    return[attr for attr in dir(obj) if not callable(getattr(obj, attr)) or callable(getattr(obj, attr)) and not attr.startswith("__")]
