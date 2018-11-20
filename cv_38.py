# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 14:14:26 2018

@author: brich
"""
'''
42. Write a Python program to find missing and additional values in two lists.
    
    Sample data: 
        Missing values in second list: b,a,c
        Additional values in second list: g,h

    Approach: 
        1) To find the missing elements of list2 we need to get the 
    difference of list1 from list2. To find the additional elements of list2,
    calculate the difference of list2 from list1.
    
        2) While finding missing elements of list1, calculate the difference    
    of list2 from list1. To find the additional elements in list1, calculate 
    the difference of list1 from list2.
    
'''

list1 = ['l','w','d','b','a','c']
list2 = ['l','w','d','g','h']

# Treat it as two sets.

# prints the missing and additional elements in list2  
print("Missing values in second list:", (set(list1).difference(list2))) 
# Make set from the list1 and make difference with the set list2
print("Additional values in second list:", (set(list2).difference(list1))) 
  
# prints the missing and additional elements in list1 
print("Missing values in first list:", (set(list2).difference(list1))) 
print("Additional values in first list:", (set(list1).difference(list2))) 

