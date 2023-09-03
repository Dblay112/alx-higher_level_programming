#!/usr/bin/python3
"""Text indentation"""

def text_indentation(text):
    """
    This function prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
    text: The text to be printed

    Raises:
    TypeError: if text is not a string
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_line = ""
    for i, char in enumerate(text):
        if char in (".", "?", ":"):
            new_line += "\n\n"
        new_line += char

    print(new_line)
