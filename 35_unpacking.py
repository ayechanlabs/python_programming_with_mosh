"""
A powerful feature in python called unpacking.
"""
coordinates = (1, 2, 3)

# coordinates[0] * coordinates[1] * coordinates[2]

# Method 1
# x = coordinates[0]
# y = coordinates[1]
# z = coordinates[2]
#
# result = x * y * z
# print(result)

# Method 2

# when a python interpreter sees this code, it will assign the first item
# to 'x', second item to 'y' and goes on.
# it doesn't only apply to tuple but also can be used with list.
x, y, z = coordinates
print(f"Values x: {x}, y: {y}, z: {z}")
result = x * y * z
print(result)
