# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 10:54:14 2018

@author: brich
"""

'''
6. Write a Python program to get a list, sorted in increasing order
by the last element in each tuple from a given list of non-empty tuples. 
Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
'''

l = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

def last(n):
    return(n[-1]) # in increasing order by the last element

def sort(l):
    return sorted(l,key = last)

print(sort(l))
