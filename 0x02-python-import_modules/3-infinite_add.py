#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    sumint = 0
    for i in range(1, len(argv)):
        sumint += int (argv[1])
    print("{}".format(sumint))
