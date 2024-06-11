power = int(input("To the power of: "))
sum = 0

result = pow(2, power)
result = str(result)
print(result)
for x in result:
    sum += int(x)
    
print(sum)