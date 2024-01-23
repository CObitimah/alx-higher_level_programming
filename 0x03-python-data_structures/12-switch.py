#!/usr/bin/python3
a = 89
b = 10
c = a
a = b
b = a
c, a, b = a, b, a
print("a={:d} - b={:d}".format(a, b))
