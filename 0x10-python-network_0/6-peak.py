#!/usr/bin/python3
"""peak-finding algorithm function"""


def find_peak(list_of_integers):
    """function to return peak"""
    if list_of_integers == []:
        return None

    peak_size = len(list_of_integers)
    if peak_size == 1:
        return list_of_integers[0]
    elif peak_size == 2:
        return max(list_of_integers)

    mid = int(peak_size / 2)
    peak = list_of_integers[mid]
    if peak > list_of_integers[mid - 1] and peak > list_of_integers[mid + 1]:
        return peak
    elif peak < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
    else:
        return find_peak(list_of_integers[mid + 1:])
