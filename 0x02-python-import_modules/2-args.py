#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    n = len(argv) - 1

    if n == 0:
        print("{} arguments.".format(n))
    elif n == 1:
        print("{} argument:".format(n))
    else:
        print("{} arguments:".format(n))

    for i in range(n):
        print("{}: {:s}".format(i + 1, argv[i + 1]))
