number = 2000000
sumPrimes = 0
prime_list = []


def isPrime(n):
    if n <= 1:
        return False

    for i in range(2, int(n / 2) + 1):
        if n % i == 0:
            return False

    return True


for x in range(number):
    print(x)
    if isPrime(x):
        prime_list.append(x)
    if x == 2000000:
        break

for x in prime_list:
    sumPrimes += x

print(sumPrimes)
