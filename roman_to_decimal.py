from pickletools import decimalnl_long
import unittest


def convert_roman_to_decimal(roman_number):
    decimal_number = 0
    for indice in range(len(roman_number)):
        letter = roman_number[indice]
        if letter == "I":
            decimal_number += 1
        if letter == "X":
            decimal_number += 10
        if letter == "V":
            decimal_number += 5
        if letter == "V" and roman_number[indice - 1] == "I" and indice != 0:
            decimal_number -= 2
        if letter == "X" and roman_number[indice - 1] == "I" and indice != 0:
            decimal_number -= 2
        if letter == "L":
            decimal_number += 50
        if letter == "L" and roman_number[indice - 1] == "X" and indice != 0:
            decimal_number -= 20
        if letter == "C":
            decimal_number += 100
        if letter == "C" and roman_number[indice - 1] == "X" and indice != 0:
            decimal_number -= 20

    return decimal_number


if __name__ == '__main__':
    unittest.main()