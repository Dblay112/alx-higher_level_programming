#!/usr/bin/python3

def divisible_by_2(my_list=[]):

    list_result = []
    for number in my_list:
        if number % 2 == 0:
            list_result.append(number)
