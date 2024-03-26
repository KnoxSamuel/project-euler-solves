# Multiples of 3 & 5

import numpy as np
import timeit

"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""

def slow_sum_of_multiples(n):
    return np.sum([i for i in range(n) if i % 3 == 0 or i % 5 == 0])

def sum_of_multiples(n):
    nums = np.arange(n)
    factors = nums[(nums % 3 == 0) | (nums % 5 == 0)]
    return np.sum(factors)

if __name__ == '__main__':
    n = 1000

    time_loop = timeit.timeit('slow_sum_of_multiples(n)', globals=globals(), number=200)
    print(f"Time using loop: {time_loop} seconds")

    time_numpy = timeit.timeit('sum_of_multiples(n)', globals=globals(), number=200)
    print(f"Time using numpy: {time_numpy} seconds")

    speed_difference = 100 * (time_loop - time_numpy) / time_loop
    print(f"np.arange is {speed_difference:.3f}% faster.")

    print(f"sum of multiples of 3 or 5 below 1000: {sum_of_multiples(n)}")
