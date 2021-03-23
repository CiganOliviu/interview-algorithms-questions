class Solution(object):

    @staticmethod
    def __reverse_number(number):

        result = 0

        while number > 0:
            digit = number % 10
            result = result * 10 + digit
            number //= 10

        return result

    def is_palindrome_number(self, number):

        return number == self.__reverse_number(number)