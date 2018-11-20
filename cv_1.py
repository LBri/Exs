# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 10:40:31 2018

@author: brich
"""
import random

a = int(input('Min of the range:'))
b = int(input('Max of the range:'))

x = random.randint(a,b+1)

while True:
    n = int(input('Your guess:'))
    
    if n > x:
        print ('No, it is less')        
    elif n < x:
        print ('No, it is more')        
    else:
        print ('Jes!', x)
        break


