# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 16:58:29 2018

@author: brich
"""

'''
18. Write a Python program to generate all permutations of a list.


import itertools

a = [1,2,3]
print(list(itertools.permutations(a)))


19. Write a Python program to get the difference between the two lists.
'''

a = [1,2,3,4]
b = [1,4]
c = (set(a) - set(b))
print(c)