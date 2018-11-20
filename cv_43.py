# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 19:10:34 2018

@author: brich
"""
'''
51. Write a Python program to split a list every Nth element. 
    Sample list: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
    Expected Output: [['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]

l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
def fn(l, n):
    return [l[i::n] for i in range(n)]
print(fn(l,2))


52. Write a Python program to compute the similarity between two lists. 
    Sample data: ["red", "orange", "green", "blue", "white"], 
                 ["black", "yellow", "green", "blue"]
    Expected Output: 
            Color1-Color2: ['white', 'orange', 'red']
            Color2-Color1: ['black', 'yellow']
'''

Color1 = ["red", "orange", "green", "blue", "white"]
Color2 = ["black", "yellow", "green", "blue"]
print(set(Color1)-set(Color2))
print(set(Color2)-set(Color1))