#!/usr/bin/python3
"""Search and update """


def append_after(filename="", search_string="", new_string=""):
    """
    Insert text after each line containing a given string in a file
    """

    text = ""
    with open(filename) as b:
        for line in b:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
