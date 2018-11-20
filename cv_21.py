# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 10:59:32 2018

@author: brich
"""

'''
7. Write a Python program to remove duplicates from a list.


def dupla(sample):
    a = []
    for x in sample:
        if x not in a:
            a.append(x)
    return(a)

sample = (1,8,4,2,1)
print(dupla(sample))

8. Write a Python program to check a list is empty or not.
'''
def check(s):
    if len(s) == 0:
        return 0
    else:
        return 1

         
sample = [2]
if check(sample):
    print('Not empty')
else:
    print('Empty')


    