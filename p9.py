"""
    Special Pythagorean Triplet
    Problem 9

    A Pythagorean triplet is a set of three natural numbers,

    a < b < c

    for which,

    a^2 + b^2 = c^2 .

    For example, 

    3^2+4^2 = 9+16 = 25 = 5^2 .

    There exists exactly one Pythagorean triplet for which 

    a + b + c = 1000 .

    Find the product a*b*c .
"""
from math import sqrt, ceil

n, m = 1, 2
bound = ceil(sqrt(500))

while not (500/m)-m == n: # target function 
    for i in range(m, bound):
        if (500/i) - i == n:
            m = i
            break
    if (500/m)-m == n: break
    n = n + 1

print(f"m: {m}, n: {n}")

a = m**2 - n**2
b = 2*m*n
c = m**2 + n**2

print(f"a: {a}, b: {b}, c: {c}")
print(f"a*b*c = {a*b*c}")

