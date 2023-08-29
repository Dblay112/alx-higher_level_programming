#!/usr/python3

def roman_to_int(roman_string):

    if not roman_string or not isinstance(roman_string, str):
        return None

    roman_num = {
      'I': 1,
      'V': 5,
      'X': 10,
      'L': 50,
      'C': 100,
      'D': 500,
      'M': 1000,
      }

    number = 0
    i = 0
    while i < len(roman_string):
        value = roman_num[roman_string[i]]
        n_value = None
        if i + 1 < len(roman_string):
            n_value = roman_num[roman_string[i]]

        if n_value and value < n_value:
            number -= value
        else:
            number += value
        i += 1

    return number
