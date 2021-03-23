import unittest

from main import Solution


class IntegerToRomanTestCase(unittest.TestCase):
    def test_case_one(self):
        solution = Solution()

        self.assertEqual(solution.convert_int_to_roman(3), 'III')

    def test_case_two(self):
        solution = Solution()

        self.assertEqual(solution.convert_int_to_roman(4), "IV")

    def test_case_three(self):
        solution = Solution()

        self.assertEqual(solution.convert_int_to_roman(9), "IX")

    def test_case_four(self):
        solution = Solution()

        self.assertEqual(solution.convert_int_to_roman(58), "LVIII")

    def test_case_five(self):
        solution = Solution()

        self.assertEqual(solution.convert_int_to_roman(1994), "MCMXCIV")


if __name__ == '__main__':
    unittest.main()
