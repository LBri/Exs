# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 10:19:15 2018

@author: brich
"""

### 2. Write a Python program to multiplies all the items in a list.
def mul_list(items):
    m = 1
    for x in items:
        m = m*x
    return m
items = [2,1,3,5,4,6,9,8,8]
print(mul_list(items))
