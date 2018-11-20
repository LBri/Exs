# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 15:27:36 2018

@author: brich
"""

'''
47. Write a Python program to insert an element before each element of a list. 

l = ['bohatstvo','zase','uz','byl','obed','nebo','ne']

l = [i for m in l for i in ('vloženo', m)]

print(l)


48. Write a Python program to print a nested lists (each list on a new line) using the print() function.
'''

l = [['bohatstvo','zase'],['uz','byl','obed'],['nebo','ne']]

#m = [ m for x in l]

print('\n'.join([str(x) for x in l]))

