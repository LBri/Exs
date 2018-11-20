# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 15:35:15 2018

@author: brich
"""
'''
34. Write a Python program using Sieve of Eratosthenes method for computing 
primes upto a specified number. 

Note:   In mathematics, the sieve of Eratosthenes, one of a number of prime 
        number sieves, is a simple, ancient algorithm for finding all prime     
        numbers up to any given limit.
'''


'''

35. Write a Python program to create a list by concatenating a given list 
which range goes from 1 to n.

Sample list : ['p', 'q']
n =5
Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']
'''
### First method: ###
sample = ['p', 'q']

def fn(sample, n):
    new_list = ['{}{}'.format(x, y) for y in range(1, n+1) for x in sample]
    return(new_list)

print(fn(sample,5))
'''
### Second method: ###

sample = ['p', 'q']

def fn(sample, n):
    for x in sample:
        for y in range(1,n+1):
            new_list = '{}{}'.format(x,y)
    #new_list = ['{}{}'.format(x, y) for y in range(1, n+1) for x in sample]
    return(new_list)

print(fn(sample,5))
'''