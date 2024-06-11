# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20

# create a number to increment and to keep checking
# check if the number is divisible by 1 .. 20
# if any of the checks fail increment the number and start over
# once it is divisible by all 1 .. 20 then print the number

number = 1
conditional = False


def is_divisible(x):
    for i in range(1, 11):
        if x % i != 0:
            return False
    return True


while not conditional:
    conditional = is_divisible(number)
    number += 1

number = number-1
print(f"{number}")
