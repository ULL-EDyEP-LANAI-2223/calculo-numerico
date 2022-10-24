#! /usr/bin/python

def gcd_iter(u, v):
    while v:
        u, v = v, u % v
    return abs(u)


print gcd_iter(50, 75)
