# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 10:21:07 2018

@author: brich
"""

### 3. Write a Python program to get the largest number from a list.

def largest_list(items):
    m = items[0]
    for x in items:
        if x > m:
            m = x
    return m
items = [28,14,35,15,42,65,59,87,88]
print(largest_list(items))
'''
### 4. Write a Python program to get the smallest number from a list.
def smallest_list(items):
    s = items[0]
    for x in items:
        if x < s:
            s = x
    return s
items = [28,14,35,15,42,65,59,87,88]
print(smallest_list(items))
'''