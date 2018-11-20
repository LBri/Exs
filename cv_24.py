# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 14:38:35 2018

@author: brich
"""

'''
Write a Python program to print a specified list after removing the 0th,
4th and 5th elements.
Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
Expected Output : ['Green', 'White', 'Black']

sample = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

#r = input()
#s = input()
#t = input()
a = [x for (i,x) in enumerate(a) if i not in (r,s,t)]
'''
sample = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

def rem(a,r,s,t):
    b = []
    for (i,x) in enumerate(a):
        if i not in (r,s,t):
            b.append(x)
    return(b)
   
print(rem(sample,0,1,5))

'''
print(str(enumerate(sample)), sample)


r = 0
s = 4
t = 5

def rem(a):
    for x in a:
        if x == a[0]:
            a.remove(x)
        if x == a[4]:
            a.remove(x)
        if x == a[5]:
            a.remove(x)
    return(a)

print(rem(sample))
'''