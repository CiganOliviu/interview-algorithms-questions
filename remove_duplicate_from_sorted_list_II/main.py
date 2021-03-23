class Solution(object):
    
    @staticmethod
    def __get_frequency_of_element(sorted_list, value):
        
        index = 0
        
        for item in sorted_list:
            if item == value:
                index += 1
    
        return index
    
    def remove_duplicate_from_sorted_list(self, sorted_list):

        result = []

        for item in sorted_list:
            if self.__get_frequency_of_element(sorted_list, item) == 1:
                result.append(item)

        return result
