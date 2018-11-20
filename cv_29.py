# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 11:37:24 2018

@author: brich
"""

'''
22. Write a Python program to find the index of an item in a specified list.

l = [1,5,8,87]
a = l.index(55)
print(a)

23. Write a Python program to flatten a shallow list. Go to the editor


import itertools
old = [[2,4,3],[1,5,6], [9], [7,9,0]]
new = list(itertools.chain(*old))
print(new)
# https://docs.python.org/2/library/itertools.html#itertools.chain


24. Write a Python program to append a list to the second list.
'''

a = [1,2,3]
b = [7,8,9]
c = a + b
print(c)

# If append used, the 'b' is treated as an appended element to the 'a' list.