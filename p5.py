# project euler p5
from math import gcd

def lcm(a, b):
    return abs(a*b) // gcd(a, b)

def smol_mult(n):
    smol = 1
    for i in range(1, n+1):
        smol = lcm(smol, i)
    return smol

smolboi = smol_mult(20)
print(smolboi)
