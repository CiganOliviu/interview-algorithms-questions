import unittest

from main import LinkedList, Solution


class SumTwoNumbersTestCase(unittest.TestCase):

    @staticmethod
    def setup_test_case_one():

        list_one = LinkedList()
        list_one.push(3)
        list_one.push(4)
        list_one.push(2)

        list_two = LinkedList()
        list_two.push(4)
        list_two.push(6)
        list_two.push(5)

        solution = Solution()
        result_list = (solution.add_two_numbers(list_one, list_two))

        return result_list

    def test_case_one_solution(self):
        result_list = self.setup_test_case_one()

        self.assertEqual(result_list.convert_to_number(), 708)

    @staticmethod
    def setup_test_case_two():

        list_one = LinkedList()
        list_one.push(0)

        list_two = LinkedList()
        list_two.push(0)

        solution = Solution()
        result_list = (solution.add_two_numbers(list_one, list_two))

        return result_list

    def test_case_two_solution(self):
        result_list = self.setup_test_case_two()

        self.assertEqual(result_list.convert_to_number(), 0)

    @staticmethod
    def setup_test_case_three():

        list_one = LinkedList()
        list_one.push(9)
        list_one.push(9)
        list_one.push(9)
        list_one.push(9)
        list_one.push(9)
        list_one.push(9)
        list_one.push(9)

        list_two = LinkedList()
        list_two.push(9)
        list_two.push(9)
        list_two.push(9)
        list_two.push(9)

        solution = Solution()
        result_list = (solution.add_two_numbers(list_one, list_two))

        return result_list

    def test_case_three_solution(self):
        result_list = self.setup_test_case_three()

        self.assertEqual(result_list.convert_to_number(), 89990001)


if __name__ == '__main__':
    unittest.main()
