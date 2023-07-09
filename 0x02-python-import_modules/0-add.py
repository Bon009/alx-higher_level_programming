#!/usr/bin/python3

a = 1
b = 2
from add_0 import add as fake_add

add(a, b) = fake_add(a, b)

print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
