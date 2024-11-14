names = ['Alex', 'Mark', 'Rico', 'Toast', 'Pai', 'Ploy']

# print out the list
print(names)

# just like the string, we can also use index to get each name from the
# list
# index: 0      1       2       3       4       5
# value: Alex   Mark    Rico    Toast   Pai     Ploy
print(names[0]) # it will print out 1st name of the list

# we can also pass negative index to list just like the string
# instead starting from 1st item of the list
# it will start last item of the list
print(names[-1])

# we can also select a range of items using colon
# it is called sub-list, and it will not modify the original list
print(names[0:3]) # it will start from index 0 up to 2
print(names[1:]) # it will start from index 1 up to the end of the list
print(names[:5]) # it will start from index 0 up to the index of 4
print(names[:]) # it will print out the whole list

# modify an item in a list
names[0] = 'Jon'
print(names)
