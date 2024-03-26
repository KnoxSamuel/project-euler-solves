# Largest Prime Factor

import numpy as np

"""
The prime factors of 13195 are 5, 7, 13, 29.

What is the largest prime factor of the number 600851475143?
"""

"""
Polland Rho's Algorithm for Integer Factorization


"""
#n = 600851475143;
n = 87625999

def prime_factors(n):
    """Returns all the prime factors of a positive integer"""
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d = d + 1
        if d*d > n:
            if n > 1: factors.append(n)
            break
    return factors


pfs = prime_factors(n)
largest_prime_factor = max(pfs)
print(f'Largest prime factor = {largest_prime_factor}')
