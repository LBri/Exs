# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 11:41:29 2018

@author: brich
"""

'''
9. Write a Python program to clone or copy a list.

old_list = [1,2,3,4,5]
def clone(old_list):
    new_list = old_list.copy()
    return(new_list)
print(clone(old_list))


10. Write a Python program to find the list of words that are longer 
than n from a given list of words.
'''
to_be_executed = ['Byl','jednou','jeden','Řek']

def fun(n,l):
    longer_than_n = []
    for x in l:
        if len(x) > n:
            longer_than_n.append(x)
    return(longer_than_n)
print(fun(3, to_be_executed))