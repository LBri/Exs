# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 17:01:22 2018

@author: brich
"""

# Write a Python function to sum all the numbers in a list. Sample List : (8, 2, 3, 0, 7). Expected Output : 20 
#l = [8, 2, 3, 0, 7] # the list -> but for the function you need a tuple

#def sum(numbers):
#    total = 0
#    for i in numbers:
#        total += i # O + i-th + (1+i)th + ...
#    return total
#print(sum(tuple(l)))

# Write a Python function to multiply all the numbers in a list.
m =[8, 2, 3, -1, 7]

def nasobeni(numbers):
    krat = 1
    for i in numbers:
        krat *= i
    return krat
print (nasobeni(tuple(m)))