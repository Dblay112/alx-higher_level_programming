#!/usr/bin/python3
"""0. Read file"""


def read_file(filename=""):
    """function that reads a text file and prints it to stdout"""

    with open(filename, encoding="utf-8") as e:
        print(e.read(), end="")
