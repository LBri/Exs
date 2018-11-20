# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 10:31:01 2018

@author: brich
"""

'''
5. Write a Python program to count the number of strings where 
the string length is 2 or more and the first and last character 
are same from a given list of strings.  
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2
'''

def count(sample_list):
    s = 0
    for x in sample_list:
        if len(x) >= 2 and x[0] == x[-1]:
            s += 1
    return(s)
    
sample = ['abc', 'xyz', 'aba', '1221']
print(count(sample))