class Solution(object):

    @staticmethod
    def __linear_search(sorted_list, searched_number):
        low = 0
        high = len(sorted_list) - 1

        while low <= high:

            mid = (high + low) // 2

            if sorted_list[mid] < searched_number:
                low = mid + 1

            elif sorted_list[mid] > searched_number:
                high = mid - 1

            else:
                return mid

        return -1

    def remove_duplicate_from_sorted_list(self, sorted_list):

        result = []

        for item in sorted_list:
            if self.__linear_search(result, item) == -1:
                result.append(item)

        return result
