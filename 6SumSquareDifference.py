rangeNumber = 101

sumRange = 0
sumSqrOfRange = 0

for x in range(rangeNumber):
    sumRange += x
    sumSqrOfRange += x * x

result = (sumRange * sumRange) - sumSqrOfRange
print(f'{sumRange} {sumSqrOfRange}')
print(f'{result}')
