# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 14:54:04 2018

@author: brich
"""

'''
13. Write a Python program to generate a 3*4*6 3D array 
whose each element is *. 


a = [[ ['*' for col in range(6)] for col in range(4)] for row in range(3)]
print(a)
'''


'''
14. Write a Python program to print the numbers of a specified list
after removing even numbers from it.
'''
a = [1,2,3,4,7,12,5]

def fn(a):
    for x in a:
        if x%2 == 0:
            a.remove(x)
    return(a)

print(fn(a))

