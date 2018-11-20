# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 10:07:54 2018

@author: brich
"""

###1. Write a Python program to sum all the items in a list.###
'''
For a range:
a = range(10)
print(sum(a))
'''

# For a list of any values:
def sum_list(items):
    s = 0
    for x in items:
        s += x
    return s
items = [2,1,3,5,4,6,9,8,8]
print(sum_list(items))
