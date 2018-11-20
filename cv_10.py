# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 17:19:05 2018

@author: brich
"""

# Write a Python program to reverse a string.
# Sample String : "1234abcd"
# Expected Output : "dcba4321"

a = '1234abcd'

def reverse(a):
    b = ''
    i = len(a) # lenght of the string to be reversed & to start the reversion
    while i > 0:
        b += a[i-1] # lower character in the string
        i = i - 1 # prepare for next step
    return b
print (reverse(a))