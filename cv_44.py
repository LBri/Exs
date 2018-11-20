# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 20:41:26 2018

@author: brich
"""
'''
53. Write a Python program to create a list with infinite elements. 
'''
# You can't have an infinite list of numbers, but you can have an infinite iterator.

import itertools
c = itertools.count()
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
'''
def arith(a, d):
   while True:
     yield a
     a += d
print (list(itertools.islice(arith(1, 2), 100)))
'''

