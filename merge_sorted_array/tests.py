import unittest

from main import Solution


class MergeSortedArray(unittest.TestCase):
    def test_case_one(self):
        solution = Solution()

        self.assertEqual(solution.merge_sorted_array([1, 2, 3], [2, 3, 4]), [1, 2, 2, 3, 3, 4])

    def test_case_two(self):
        solution = Solution()

        self.assertEqual(solution.merge_sorted_array([-1, -2, -3], [-4, -5, -6]), [-6, -5, -4, -3, -2, -1])


if __name__ == '__main__':
    unittest.main()
