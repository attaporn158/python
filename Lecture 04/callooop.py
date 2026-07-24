num_max = int(input('How many numbers do you want to sum? '))

total = 0.0

print('This program calculates the sum of')
print(num_max, 'numbers you will enter.')

for counter in range(num_max):
    number = int(input('Enter a number: '))
    total += number

print('The sum is:', total)