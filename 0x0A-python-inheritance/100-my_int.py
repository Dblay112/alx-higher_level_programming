#!/usr/bin/python3
"""12. My integer """


class MyInt(int):
    """class MyInt that inherits from int
    """

    def __eq__(self, other):
        return (int(self) != other)

    def __ne__(self, other):
        return (int(self) == other)
