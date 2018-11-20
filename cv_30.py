# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 12:04:12 2018

@author: brich
"""

'''
25. Write a Python program to select an item randomly from a list. Go to the editor
Click me to see the sample solution

import random
l = ['a','b','c','d','e']
print(random.choice(l))

26. Write a python program to check whether two lists are circularly identical
'''
# Using map() function:

# https://docs.python.org/3/library/functions.html#map

# Using Python’s inbuilt function map() we can do this in one single step, 
# where we have to map list2 in a string and then see if it exists in the 
# mapping of twice of list1 (2*list1) in another string.

# function to check circularly identical or not 
def circularly_identical(list1, list2): 
     
    return(' '.join(map(str, list2)) in ' '.join(map(str, list1 * 2))) 
      
  
# driver code 
list1 = ['a','b','c','d','e']
list3 = ['e','a','b','c','d']
list2 = ['e','a','b','d','c']
  
  
# check for list 1 and list 2  
if(circularly_identical(list1, list2)): 
    print("Yes" )
else: 
    print("No")
  
# check for list 2 and list 3  
if(circularly_identical(list2, list3)): 
    print("Yes")
else: 
    print("No")