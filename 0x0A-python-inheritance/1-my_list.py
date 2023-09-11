#!/usr/bin/python3
"""1. My list """


class MyList(list):
    """class called list"""
    def print_sorted(self):
        """prints a list but sorted"""
        self.sort()
        print(self)
