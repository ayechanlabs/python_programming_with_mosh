# Version 1
for x in range(2):
    print('x' * 5)
    for y in range(0, 3, 2):
        if x == 0:
            print('x' * 2)
            break
        else:
            print('x' * 2)

# Version 2
numbers = [5, 2, 5, 2, 2]

# for count in numbers:
#     # print(count) # it will print each number from list
#     print('x' * count)

for counter in numbers:
    output = ''
    for count in range(counter):
        output += 'x'
    print(output)

# Exercise: print letter 'L' using '*'
