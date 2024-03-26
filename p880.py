"""
The problem states:

`(x, y)` is called a nested radical pair if `x` and `y` are non-zero integers such that `x / y` is not a cube of a rational number, and there exist integers `a`, `b`, and `c` such that:
sqrt( cbrt(x) + cbrt(y) ) == cbrt(a) + cbrt(b) + cbrt(c)

For example, both `(-4, 125)` and `(5, 5324)` are nested radical pairs:
sqrt( cbrt(-4) + cbrt(125) ) == cbrt(-1) + cbrt(2) + cbrt(4)
sqrt( cbrt(5) + cbrt(5324) ) == cbrt(-2) + cbrt(20) + cbrt(25)

Let H(N) be the sum of `abs(x) + abs(y)` for all the nested radical pairs `(x, y)` where `abs(x) <= abs(y) <= N`.
For example, H(10**3) = 2535.

Find H(10^15).
"""

from math import gcd, cbrt
from cmath import isclose, sqrt as csqrt
from sympy import symbols, solve, Eq, root
import numbers

def is_real(n):
    print("in is_real(n)...")
    return isinstance(n, numbers.Real)

def complex_to_real(c):
    print("in complex_to_real(c)...")
    if c.imag == 0:
        return c.real
    else:
        raise ValueError("Cannot convert a complex number with a non-zero imaginary part to a real number.")

def is_cube_of_rational(x, y):
    print("in is_cube_of_rational(x, y)...")
    """Checks if x/y is a cube of a rational number."""
    if y == 0:
        return False
    d = gcd(x, y)
    x, y = x // d, y // d
    return cbrt(x).is_integer() and y == 1

def satisfies_nested_radical(x, y):
    """Checks if the pair (x, y) satisfies the nested radical condition."""
    lhs = csqrt(cbrt(x) + cbrt(y))
    
    a, b, c = symbols('a b c', real=True)
    equation = Eq(root(a, 3) + root(b, 3) + root(c, 3), lhs)
    
    solutions = solve(equation, (a, b, c), dict=True)
    print("finished solving solutions in satisfies_nested_radicals(x, y)...") #debug

    for sol in solutions:
        real_solution = True
        for val in sol.values():
            if not is_real(val.evalf()):
                real_solution = False
                break
        if real_solution:
            print("solutions loop check = True...") #debug
            return True
    print("solutions loop check = False") #debug
    return False
    

def H(N):
    total_sum = 0
    for x in range(-N, N + 1):
        for y in range(x, N + 1):
            if x != 0 and y != 0 and not is_cube_of_rational(x, y):
                if satisfies_nested_radical(x, y):
                    lhs = csqrt(cbrt(x) + cbrt(y))
                    rhs = cbrt(x) + cbrt(y)
                    # Convert complex numbers with zero imaginary part to real
                    if lhs.imag == 0:
                        lhs = complex_to_real(lhs)
                    if rhs.imag == 0:
                        rhs = complex_to_real(rhs)
                    if isclose(abs(lhs), abs(rhs), rel_tol=1e-9):
                        total_sum += abs(x) + abs(y)
    return total_sum

# H(10^3)
print(H(10**3))
