import unittest

from main import Solution


class RemoveDuplicateFromSortedListTestCase(unittest.TestCase):
    def test_case_one(self):
        solution = Solution()

        self.assertEqual(solution.remove_duplicate_from_sorted_list([1, 1, 2, 3, 3]), [1, 2, 3])


if __name__ == '__main__':
    unittest.main()
