# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 13:24:55 2018

@author: brich
"""

'''
60. Write a Python program to find a tuple, the smallest second index value from a list of tuples.

x = [(4, 1), (1, 2), (6, 0)]
print(min(x, key=lambda n: (n[1], -n[0])))


61. Write a Python program to create a list of empty dictionaries.

m = 5
l = [{} for x in range(m)] #list comprehension
print(l)

62. Write a Python program to print a list of space-separated elements.
'''
# So instead of , I want _?

l = ['a','b','c']
print(*l, end = ' ')

'''
Named parameters occurring after *args in the parameter list must be specified 
using keyword syntax in the call. You can also use a bare * in the parameter 
list to indicate that you don’t accept a variable-length argument list, but you
do have keyword-only arguments. --> Define then end = ' '.
'''