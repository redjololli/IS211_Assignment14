
#Assignment 14

def fibonacci(n):
        # First Fibonacci number is 0
    if n == 1:
        return 0
    # Second Fibonacci number is 1
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def gcd(a, b):
    r = a % b

    if b > a:
        return gcd(b, a)
    if r == 0:
        return b
    else:
        return gcd(b, r)


def compareTo(s1, s2):
    if s1 < s2:
        return - 1
    elif s1 == s2:
        return 0
    elif s1 > s2:
        return 1
