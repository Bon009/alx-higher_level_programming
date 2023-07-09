#!/usr/bin/python3
a = 1
b = 2
from add_0 import add as fake_add

result = fake_add(a, b)
print("{:d} + {:d} = {:d}".format(a, b, result))
