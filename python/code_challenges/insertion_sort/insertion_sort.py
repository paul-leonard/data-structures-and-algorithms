'''


'''

def insertionSort(integer_array):
    for i in range(len(integer_array)):
        min_index_so_far = i

        start = i + 1
        for j in range(start,len(integer_array)):
            if integer_array[j] < integer_array[min_index_so_far]:
                min_index_so_far = j

        temp = integer_array[min_index_so_far]
        integer_array[min_index_so_far] = integer_array[i]
        integer_array[i] = temp

    return integer_array
    # return [7,7,7]
