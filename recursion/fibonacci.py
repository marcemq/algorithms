#!/usr/bin/python

def recFibonacci(n):
    if n == 0:
        return 0
    elif n ==1:
        return 1
    else:
        return recFibonacci(n-2) + recFibonacci(n-1)

if __name__ == "__main__":
    n = int(input())
    fn = recFibonacci(n)
    print(fn)
