# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 16:10:25 2018

@author: brich
"""

# Write a Python program to construct the following pattern, using a nested for loop.
# nested loop = a loop inside a loop

# Exapmle of a nested loop:
#for i in range(1,11):
#   for j in range(1,11):
#      k = i*j
#      print (k, end=' @ ') # By default python’s print() function ends with a newline. 
      # Python’s print() function comes with a parameter called ‘end’. 
      # By default, the value of this parameter is ‘\n’, i.e. the new line character. 
      # You can end a print statement with any character/string using this parameter.
      # Therefore, instead of 1 2 3 ..., it prints: 1 @ 2 @ 3 @ ...
#   print()
   
### The RANGE fn ###
# It generates a list of numbers, which is generally used to iterate over with for loops

# The solution of the task:
n=5;
# Stars rising
for i in range(n): # row
    for j in range(i): # column
        print ('* ', end="")
    print('')

# Stars lowering
for i in range(n,0,-1): #row
    for j in range(i): # column
        print('* ', end="")
    print('')
    
# Check the type:
print (type(range(n,0-1)))