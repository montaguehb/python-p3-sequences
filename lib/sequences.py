#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
        return print([])
    elif length == 1:
        return print([0])
    fib = [0, 1]
    for x in range(length - 2):
        fib.append(fib[-1] + fib[-2])
    print(fib)