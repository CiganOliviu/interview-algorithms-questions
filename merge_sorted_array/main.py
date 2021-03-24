class Solution(object):

    @staticmethod
    def __sort_array(a_list):

        result = a_list

        for i in range(0, len(result) - 1, 1):
            for j in range(i + 1, len(result), 1):
                if result[i] > result[j]:
                    result[i], result[j] = result[j], result[i]

        return result

    def merge_sorted_array(self, nums_list_one, nums_list_two):

        result = nums_list_one

        for item in nums_list_two:
            result.append(item)

        return self.__sort_array(result)

