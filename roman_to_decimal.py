def convert_roman_to_decimal(roman_number):
    decimal_number = 0
    roman_number = roman_number.upper()
    roman_to_decimal = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }
    for i in range(len(roman_number)):
        if i > 0 and roman_to_decimal[roman_number[i]] > roman_to_decimal[roman_number[i - 1]]:
            decimal_number += roman_to_decimal[roman_number[i]] - 2 * roman_to_decimal[roman_number[i - 1]]
        else:
            decimal_number += roman_to_decimal[roman_number[i]]
    return decimal_number
