"""
You are given two non-empty linked lists representing two non-negative integers.

The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return
the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""


class ListNode(object):
    def __init__(self, val, next_element=None):
        self.val = val
        self.next = next_element


class LinkedList(object):
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = ListNode(new_data)
        new_node.next = self.head
        self.head = new_node

    def output(self):
        current = self.head

        while current:
            print(current.val, end=" ")
            current = current.next

    @staticmethod
    def __create_number(current, result):

        while current:
            result = result * 10 + current.val
            current = current.next

        return result

    def convert_to_number(self):
        current = self.head

        result = 0

        result = self.__create_number(current, result)

        return result


class Solution(object):

    @staticmethod
    def __create_list(number, result):
        while number:
            digit = number % 10
            result.push(digit)

            number //= 10

    @staticmethod
    def __convert_number_to_list(number):
        result = LinkedList()

        Solution.__create_list(number, result)

        return result

    @staticmethod
    def __reverse_number(number):

        result = 0

        while number:
            digit = number % 10
            result = result * 10 + digit
            number //= 10

        return result

    def add_two_numbers(self, linked_list_one, linked_list_two):
        first_number = linked_list_one.convert_to_number()
        second_number = linked_list_two.convert_to_number()

        sum_of_numbers = self.__reverse_number(first_number + second_number)

        return self.__convert_number_to_list(sum_of_numbers)