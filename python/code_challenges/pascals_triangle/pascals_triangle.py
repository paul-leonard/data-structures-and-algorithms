'''
Required Features:
- [x] The rows continue on forever. Assuming that row N = 1 corresponds to that first row, [1], write a function that takes in N as a value and prints the first N rows of Pascal’s Triangle.
'''

def create_pascals_triangle(n):
    if type(n) is not int or n == 0:
        print("Invalid input.")
        return None

    pascals_triangle = [[1],]

    for i in range (n-1):
        pascals_triangle.append(next_row_of_pascals(pascals_triangle[i]))
    return pascals_triangle


def next_row_of_pascals(prev_row):
    new_row =[prev_row[0],]
    for i, value in enumerate(prev_row[:-1]):
        new_row.append(value + prev_row[i+1])
    new_row.append(prev_row[-1])
    return new_row

def print_pascals_triangle(pascals_triangle):
    if not pascals_triangle:
        return None

    for row in pascals_triangle:
        # print(*row)
        string_version = ""
        for number in row:
            string_version += " " + str(number) + " "
        print(string_version.center(160))

# manual tests
print_pascals_triangle(create_pascals_triangle("cat"))
print_pascals_triangle(create_pascals_triangle(0))
print_pascals_triangle(create_pascals_triangle(1))
print_pascals_triangle(create_pascals_triangle(2))
print_pascals_triangle(create_pascals_triangle(3))
print_pascals_triangle(create_pascals_triangle(7))
print_pascals_triangle(create_pascals_triangle(10))







# Robert Radford's code for printing a very nicely spaced triangle
def print_staggered(triangle):
	# Find the largest value to size things off of, and use its length for it
	largest_num = triangle[-1][len(triangle[-1])//2]
	zero_count = len(str(largest_num))

	# Create the print string for the last row first to use it as a size reference
	len_str = f'{triangle[-1][0]}'
	for item in triangle[-1][1:]:
		len_str += ' '*(zero_count+1-len(str(item)))+str(item)

	# create the rest of the rows centered on the last rows length
	for step in triangle[:-1]:
		string = f'{step[0]}'
		for item in step[1:]:
			string += ' '*(zero_count+1-len(str(item)))+str(item)
		string+=' '*zero_count
		print(string.center(len(len_str)+zero_count, ' '))

	# print the last row formatted earlier
	print(len_str)
