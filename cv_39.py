# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 14:28:39 2018

@author: brich
"""

'''
43. Write a Python program to split a list into different variables.

l = [('alpha','beta','omega'),('gama','nu','mu'),('delta','lambda','epsilon')]

raz,dva,tri = l

print(raz)


44. Write a Python program to generate groups of five consecutive numbers in a list.
'''
l = [[5*i + j for j in range(1,6)] for i in range(5)]

print(l)