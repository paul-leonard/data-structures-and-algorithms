'''
Required Features:
- [x] create a function which takes in an integer array and returns an array of the same values sorted ascendingly
'''

def insertionSort(integer_array):
    ''' input: integer array;  output: integer array of the same values sorted ascendingly;  This function sorts an array in the order of increasing values. '''
    for i in range(len(integer_array)):
        min_index_so_far = i

        start_j_index = i + 1
        for j in range(start_j_index,len(integer_array)):
            if integer_array[j] < integer_array[min_index_so_far]:
                min_index_so_far = j

        temp = integer_array[min_index_so_far]
        integer_array[min_index_so_far] = integer_array[i]
        integer_array[i] = temp

    return integer_array
