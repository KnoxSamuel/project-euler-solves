# project euler p7
# 10 0001st Prime

from math import floor, sqrt

p = 0
n = 2

while p != 10001:
    flag = True

    for i in range(2, floor(sqrt(n)) + 1):
        if n % i == 0:
            flag = False
            break

    if flag == True:
        p = p + 1
        print(f"{p}th: {n}")

    n = n + 1

