def is_triangle(number):
    if number > 0:
        if number % (number*(number+1)/2) == number:
            return True


def number_of_divisor(number):
    count = 0

    half = 0
    if number % 2 == 0:
        half = number/2
    else:
        half = (number+1)/2

    for x in range(int(half), 0, -1):
        if number % x == 0:
            count += 1

    return count + 1


number = 76576500
# print(is_triangle(number))
print(number_of_divisor(number))
print(is_triangle(76576500))

# for x in range(76576500):
#     if is_triangle(x):
#         if number_of_divisor(x) >= 500:
#             print(x)
