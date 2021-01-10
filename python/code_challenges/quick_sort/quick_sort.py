'''
Required Features:
- [ ] create a function which takes in an integer array and returns an array of the same values sorted in ascending order using a "quick sort" algorithm
'''

def quick_sort(integer_array, left, right):
    ''' input: integer array, left index position, right index position;  output: integer array of the same values sorted ascendingly;  This function sorts an array in ascending order using a quick sort algorithm. '''

    if left < right:
        end_pivot_index = partition(integer_array, left, right)
        quick_sort(integer_array, left, end_pivot_index - 1)
        quick_sort(integer_array, end_pivot_index + 1, right)

def partition(integer_array, left, right):
    pivot_value = integer_array[right]

    low = left - 1

    # for
    #     if integer_array[i] <= pivot_value:
    #         low += 1
    #         swap(integer_array, i, low)




