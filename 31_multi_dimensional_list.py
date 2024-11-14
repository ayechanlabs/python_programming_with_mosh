"""
In this exercise, we're going to learn about a multidimensional
list or 2-dimensional list.

What is 2-dimensional list or multidimensional list?
2D List is a list, which is a collection of 1D list.
"""

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# print the result
print(matrix)

# print out the 1st line of the list
# it will print out the inner list
print(matrix[0]) # it will return the 1st in the 2D list.

# print out the 1st item of the 2D list
# 2d_list[row][col]
print(matrix[0][0])

# modify an item in the 2d list
matrix[0][0] = 10

print(matrix) # print a whole 2d list
print(matrix[0][0]) # print the 1st item of the 2d list
print(matrix[0][-1]) # 3
print(matrix[-1][0]) # 7
print(matrix[-1][-1]) # 9


# we can also use nested loop to iterate all the item from the 2d list
for lst in matrix:
    for item in lst:
        print(item)
