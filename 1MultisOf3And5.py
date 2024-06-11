low = int(input('Low number: '))
high = int(input('High number: '))
result = 0

for x in range(low, high):
    if x%3 == 0:
        result += x
    elif x%5 == 0:
        result += x

print(f'The sum of the multiples of 3 or 5 is {result}')
