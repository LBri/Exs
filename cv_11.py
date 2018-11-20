# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 17:35:27 2018

@author: brich
"""

# Write a Python function to check whether a number is in a given range.

start = int(input('Insert start:'))
stop = int(input('Insert stop:'))
rang = range(start, stop)
    
def check(rang):
    number = int(input('Which number:'))
    
    if number in rang:
        print ('The number', number, 'is in the range')
    else:
        print ('The number', number, 'is not in the range')
    return 

check(rang)