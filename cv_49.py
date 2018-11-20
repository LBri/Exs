# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 16:42:39 2018

@author: brich
"""

'''
65. Write a Python program to access dictionary keys element by index.
'''
dic = {'a':1,'b':2,'c':3}
print(list(dic)[2])

'''
66. Write a Python program to find the list in a list of lists whose sum of 
elements is the highest. 
    Sample lists: [1,2,3], [4,5,6], [10,11,12], [7,8,9]
    Expected Output: [10, 11, 12]
'''

find = [[1,2,3], [4,5,6], [10,11,12], [7,8,9]]
print(max(find, key=sum))

