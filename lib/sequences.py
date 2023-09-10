#!/usr/bin/env python3

def print_fibonacci(length):
    
    if length == 0:
        fibonacci = []
        print(fibonacci)
    elif length == 1:
        fibonacci = [0]
        print(fibonacci)
    else:
        fibonacci = [0, 1]
        for n in range(length-2):
            fibonacci.append(fibonacci[-1] + fibonacci[-2])
        print(fibonacci)