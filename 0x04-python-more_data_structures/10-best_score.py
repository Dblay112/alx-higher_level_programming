#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    maxi = None
    maxi_1 = None
    for key, value in a_dictionary.items():
        if maxi is None or value > maxi:
            maxi = value
            maxi_1 = key

    return maxi_1
