# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 21:21:46 2018

@author: brich
"""

# Write a Python program to calculate the sum of a list of numbers. 
# l = list; s = sum
# def l_sm(l):
#    if len(l) == 1:
#        return l[0]
#    else:
#        return l[0] + l_sm(l[1:])
    
#print (l_sm([2,4,6,9,6,3,0,3]))

# Write a Python program of recursion list sum.
# Test Data: [1, 2, [3,4], [5,6]]
# Expected Result: 21

def rec_list_sum(l):
    tot = 0
    for element in l:
        if type(element) == type([]):
            tot = tot + rec_list_sum(element)
        else:
            tot = tot + element
    
    return tot
print (rec_list_sum([1, 2, [3,4], [5,6]]))

# Write a Python program to find the greatest common divisor (gcd) of two integers.

def Recurgcd(a, b):
	low = min(a, b)
	high = max(a, b)

	if low == 0:
		return high
	elif low == 1:
		return 1
	else:
		return Recurgcd(low, high%low)
print(Recurgcd(12,14))