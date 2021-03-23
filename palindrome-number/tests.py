import unittest

from main import Solution


class PalindromeNumberTestCase(unittest.TestCase):
    def test_case_one(self):
        solution = Solution()

        self.assertEqual(solution.is_palindrome_number(123), False)

    def test_case_two(self):
        solution = Solution()

        self.assertEqual(solution.is_palindrome_number(12321), True)

    def test_case_three(self):
        solution = Solution()

        self.assertEqual(solution.is_palindrome_number(1), True)

    def test_case_four(self):
        solution = Solution()

        self.assertEqual(solution.is_palindrome_number(1234321), True)


if __name__ == '__main__':
    unittest.main()
