class Solution(object):
    @staticmethod
    def reverse_number(number):

        reverse = 0

        while number > 0:
            digit = number % 10
            reverse = reverse * 10 + digit
            number //= 10

        return reverse

