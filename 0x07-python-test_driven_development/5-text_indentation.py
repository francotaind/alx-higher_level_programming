#!/usr/bin/python3

"""Defines a text-indentation function."""


def text_indentation(text):
    """Print text with two new lines after each '.', '?', and ':'.

    Args:
        text (string): The text to print.
    Returns: None.
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    string = ""
    specials = ['.', '?', ':']
    for ch in text:
        string += ch
        if ch in specials:
            string += "\n\n"
    print(string, end='')
