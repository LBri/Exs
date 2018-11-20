# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 13:09:27 2018

@author: brich
"""

'''
29. Write a Python program to get unique values from a list. 

a = [84,65,46,9,84,9]

def uniq(a):
    b = set() # set an empty set
    for x in a:
        b.add(x)

    return (b)

print(list(uniq(a)))

30. Write a Python program to get the frequency of the elements in a list.
'''

from collections import Counter

a = [84,65,46,9,84,9]

print(Counter(a))