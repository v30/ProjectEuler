maxElement = int(input('Max element value: '))
num = 0
num1 = 0
num2 = 1
result = 0

while num < maxElement:
    num = num1 + num2
    num1 = num2
    num2 = num
    if num%2 == 0:
        result += num

print(f'Count of all the even elements under a max value is {result}')