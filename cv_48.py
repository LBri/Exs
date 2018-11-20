# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 16:05:41 2018

@author: brich
"""
'''
63. Write a Python program to insert a given string at the beginning of all items in a list. 
    Sample list : [1,2,3,4], string : emp
    Expected output : ['emp1', 'emp2', 'emp3', 'emp4']

What I tried first:
l = [1,2,3,4]
l = [i for m in l for i in ('emp' + str(m)]
print(l)
'''
num = [1,2,3,4]
print(['emp{number}'.format(number = i) for i in  num])

'''
64. Write a Python program to iterate over two lists simultaneously.
'''

num = [1, 2, 3]
alf = ['A', 'B', 'C']
for (a,b) in zip(num, alf):
     print(a, b)