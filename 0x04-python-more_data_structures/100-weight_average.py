#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    sum_scores = 0
    weight_scores = 0
    
    for score, weight in my_list:
        sum_scores += score * weight
        weight_scores += weight

    return sum_scores / weight_scores
