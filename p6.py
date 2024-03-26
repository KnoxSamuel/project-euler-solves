# project euler p6
# sum square difference

def sum_of_square(num):
    n = 0
    for i in range(1, num+1):
        n += i**2
    return n

def square_of_sum(num):
    n = 0
    for i in range(1, num+1):
        n += i
    return n**2

sum_square = sum_of_square(100)
square_sum = square_of_sum(100)

print(square_sum - sum_square)
