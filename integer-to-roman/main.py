class Solution(object):

    __roman_digits_correlation = \
        {'I': 1,
         'IV': 4,
         'V': 5,
         'IX': 9,
         'X': 10,
         'XL': 40,
         'L': 50,
         'XC': 90,
         'C': 100,
         'CD': 400,
         'D': 500,
         'CM': 900,
         'M': 1000
         }

    __roman_digits = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

    def __is_passing_roman_digit(self, number, digit):
        return number >= self.__roman_digits_correlation[digit] and number > 0

    def convert_int_to_roman(self, number):

        result = ""

        for digit in self.__roman_digits:
            while self.__is_passing_roman_digit(number, digit):
                number -= self.__roman_digits_correlation[digit]
                result += digit

        return result

