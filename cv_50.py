# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 16:43:29 2018

@author: brich
"""

'''
67. Write a Python program to find all the values in a list are greater 
than a specified number. 
'''
l = [40, 50, 60, 10, 20, 30]
m = []
for x in l:
    if x >30:
        m.append(x)
print(m)
'''
68. Write a Python program to extend a list without append. 
'''
a = [10, 20, 30]
b = [40, 50, 60]
a.extend(b)
print(a)