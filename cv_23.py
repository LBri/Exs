# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 14:25:43 2018

@author: brich
"""

'''
11. Write a Python function that takes two lists and returns True 
if they have at least one common member.
'''
a1 = [1,3,5,4,8]
a2 = [84,65,46,9]

def compare(fn1, fn2):
    result = False
    for x in fn1:
        for y in fn2:
            if x == y:
                result = True
    return (result)

print(compare(a1,a2))
    
