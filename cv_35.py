# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 16:24:26 2018

@author: brich
"""
'''
36. Write a Python program to get variable unique identification 
    number or string. 

x = 1968
print(format(id(x), 'x'))
s = 'Medved'
print(format(id(s), 'x')) 

37. Write a Python program to find common items from two lists.
'''
a1 = [1,3,5,4,8]
a2 = [84,65,46,9]

# Compare it as sets:

c = (set(a1) and set(a2))
print(list(c))

'''
def common(fn1, fn2):
    result = []
    for x in fn1:
        for y in fn2:
            if x == y:
                result.append(x) 
                result.append(y)
    return(result)

print(common(a1,a2))
'''