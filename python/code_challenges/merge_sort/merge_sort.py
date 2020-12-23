'''
Required Features:
- [x] create a function which takes in an integer array and returns an array of the same values sorted in ascending order using a "merge sort" algorithm
'''

def merge_sort(integer_array):
    ''' input: integer array;  output: integer array of the same values sorted ascendingly;  This function sorts an array in the order of increasing values. '''

    n = len(integer_array)

    if n > 1:
        mid_index = n // 2
        left = integer_array[0:mid_index]
        right = integer_array[mid_index:]

        merge_sort(left)
        merge_sort(right)
        merge(left, right, integer_array)

    return integer_array

def merge(left, right, integer_array):
    l_index = 0
    r_index = 0
    output_index = 0

    while l_index < len(left) and r_index < len(right):
        if left[l_index] <= right[r_index]:
            integer_array[output_index] = left[l_index]
            l_index += 1
        else:
            integer_array[output_index] = right[r_index]
            r_index += 1

        output_index += 1

    if l_index == len(left):
        while r_index < len(right):
            integer_array[output_index] = right[r_index]
            r_index += 1
            output_index += 1
    else:
        while l_index < len(left):
            integer_array[output_index] = left[l_index]
            l_index += 1
            output_index += 1
