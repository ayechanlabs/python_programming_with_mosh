numbers = [2, 2, 4, 6, 3, 4, 6, 1]
unique_numbers = []

for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)

print(f'Unique Numbers: {unique_numbers}')
