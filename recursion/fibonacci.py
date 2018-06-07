#!/usr/bin/python
from functools import lru_cache

def recFibonacci(n):
    """Recursive Fibonacci function. """
    if n <= 0:
        return 0
    elif n ==1:
        return 1
    else:
        return recFibonacci(n-2) + recFibonacci(n-1)

def nemoFibonacci(n, nemo):
    """Recursive Fibonacci function with nemoization. """
    if n <= 0:
        return 0
    elif n ==1:
        return 1
    elif nemo[n] == 0:
        nemo[n] = nemoFibonacci(n-2, nemo) + nemoFibonacci(n-1, nemo)
    return nemo[n]

def itFibonacci(n):
    """Iterative  Fibonacci function."""
    i, a, b = 0, 0, 1
    while i != n:
        a, b = b, a+b
        i += 1
    return a

@lru_cache(maxsize=None)
def dynFibonacci(n):
    """Recursive fibonacci with memoization from the stdlib."""
    if n < 2:
        return n
    return dynFibonacci(n-1) + dynFibonacci(n-2)

if __name__ == "__main__":
    n = int(input())
    nemo = [0] * (n+1)
    fn = recFibonacci(n)
    print(fn)
    fn = itFibonacci(n)
    print(fn)
    fn = nemoFibonacci(n, nemo)
    print(fn)
    fn = dynFibonacci(n)
    print(fn)
