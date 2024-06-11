primePos = int(input("Prime number: "))
primesFound = 0
number = 1
primes = []


def isPrime(n):
    if n <= 1:
        return False

    for i in range(2, int(n/2)+1):
        if n % i == 0:
            return False

    return True


while primesFound < primePos:
    if isPrime(number):
        primesFound += 1
        primes.append(number)

    number += 1

primes.sort(reverse=True)
print(primes)
