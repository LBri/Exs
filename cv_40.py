# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 15:02:23 2018

@author: brich
"""


'''
45. Write a Python program to convert a pair of values into a sorted unique array. 
'''
import numpy as np
values = [(1,2),(8,4),(2,1),(3,6),(7,9)]
print(np.unique(values))

'''
46. Write a Python program to select the odd items of a list. 
'''

l = ['bohatstvo','zase','uz','byl','obed','nebo','ne']
m = []
for x in range(0,len(l)):
    if x%2 != 0:
        m.append(x)
print(m)

# If meant at the second position - slice it:
#print(l[::2])