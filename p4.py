# projecteuler p4

def largest_palindrome(k):
    max = 0
    for i, n in enumerate(k):
        r = reverse(n)
        if r == n and r > max:
            max = r
            print("current=", max) 
    return max

def init_list(k):
    #i, j = 100, 100
    for i in range(100, 1000):
        for j in range(100, 1000):
            k.append(i*j)
    return k

def reverse(n):
    r_str = str(n)[::-1]
    r_int = int(r_str)
    return r_int

k = []
k = init_list(k)
print("largest=", largest_palindrome(k))
print("length of k=", len(k))
