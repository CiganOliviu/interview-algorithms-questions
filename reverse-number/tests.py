import unittest

from main import Solution


class ReverseNumber(unittest.TestCase):
    def test_case_one(self):
        solution = Solution()

        self.assertEqual(solution.reverse_number(123), 321)

    def test_case_two(self):
        solution = Solution()

        self.assertEqual(solution.reverse_number(76), 67)


if __name__ == '__main__':
    unittest.main()
