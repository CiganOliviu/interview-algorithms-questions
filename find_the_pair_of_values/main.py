def __sort_array(a_list):
    result = a_list

    for i in range(0, len(result) - 1, 1):
        for j in range(i + 1, len(result), 1):
            if result[i] > result[j]:
                result[i], result[j] = result[j], result[i]

    return result


def find_the_pair_of_values(first_array, second_array):
    __sort_array(first_array)
    __sort_array(second_array)

    minimum_value = 999999999
    result = [None, None]

    it = 0
    jit = 0

    while it < len(first_array) and jit < len(second_array):

        if minimum_value > abs(first_array[it] - second_array[jit]):
            result[0] = first_array[it]
            result[1] = second_array[jit]
            minimum_value = abs(first_array[it] - second_array[jit])

        if first_array[it] < second_array[jit]:
            it += 1

        else:
            jit += 1

    return result


if __name__ == '__main__':
    print(find_the_pair_of_values([4, 17, 3, 49, 9], [127, 36, 7, 220, 25, 70]))
