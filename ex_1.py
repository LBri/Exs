# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 18:52:41 2018

@author: brich
"""

total_sum = 0
a = int(input('Set:'))
if a == 0:
    break
else:
    total_sum += a
    if total_sum >= 21:
        print('Total sum is', total_sum)
        break
#a = int(input())
#else:
    #print('Total sum is less than 21 and is equal to', total_sum, '.')