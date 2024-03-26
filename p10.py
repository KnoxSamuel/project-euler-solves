# Summation of Primes Below 2,000,000

from math import floor, sqrt

p = 0 # index of prime
n = 2 # range [1st prime (2), 2_000_000]
c = 0 # sum of primes

while n < 100:
    flag = True

    for i in range(2, floor(sqrt(n)) + 1):
        if n % i == 0:
            flag = False
            break

    if flag == True:
        c = c + n
        p = p + 1
        print(f"{p}th: {n}")

    n = n + 1

print("sum n < 2,000,000 = ", c)

