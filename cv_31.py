# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 12:14:22 2018

@author: brich
"""

'''
27. Write a Python program to find the second smallest number in a list. 

import heapq

l = [84,45, 12,78,123]

def fn(numbers):
    return heapq.nsmallest(2, numbers)[-1]
print(fn(l))

#28. Write a Python program to find the second largest number in a list.
'''
import heapq

l = [84,45, 12,78,123,211]

def fn(numbers):
    return heapq.nlargest(2, numbers)[-1]
print(fn(l))