# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 17:41:32 2018

@author: brich
"""

# Write a Python function to calculate the factorial of a number (a non-negative integer).
# The function accepts the number as an argument.

number = int(input('Factorial of number:'))

def factorial(num):
    if num == 0:
        return(1)
    else:
        return num*factorial(num-1) # rekurzíva
    
print(factorial(number))