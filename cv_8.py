# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 16:39:07 2018

@author: brich
"""

# Write a Python function to find the Max of three numbers.

a = int(input('Set a:'))
b = int(input('Set b:'))
c = int(input('Set c:'))
    
def Max(a,b,c):
    "Find max of three numbers"
    if a > b and a > c:
        print ('The number', a ,'is the largest number.')
    elif a > b and a < c:
        print ('The number', c ,'is the largest number.')
    elif b > a and b > c:
        print ('The number', b ,'is the largest number.')
    return

Max(a,b,c)




# Purpose of the 'return' function:
    # The print() function writes, i.e., "prints", a string in the console. 
    # The return statement causes your function to exit and hand back a value
    # to its caller. The point of functions in general is to take in inputs and 
    # return something. The return statement is used when a function is ready 
    # to return a value to its caller.
    
    