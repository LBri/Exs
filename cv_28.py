# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 17:19:13 2018

@author: brich
"""

'''
20. Write a Python program access the index of a list. 

l = [1,2,3,4,5]
for x in l:
    print(l.index(x), x)


21. Write a Python program to convert a list of characters into
a string.
'''

l =  ['a','b','c']


def fn(l):
    s = "" 
    for x in l:
        s += x
    return(s)

print(fn(l))

