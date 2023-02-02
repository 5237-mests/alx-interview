#!/usr/bin/python3
"""Module
"""
from sys import argv, exit

Nn = argv[1]
if Nn.isdigit():
    N = int(Nn)
else:
    N = Nn

if len(argv) > 2:
    print("Usage: nqueens N")
    exit(1)
elif type(N) != int:
    print("N must be a number")
    exit(1)
elif N < 4:
    print("N must be at least 4")
    exit(1)
