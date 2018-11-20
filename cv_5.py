# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 13:13:20 2018

@author: brich
"""
import random


with open('sowpods.txt') as f: # Read all the lists of words
	words = list(f)
print(random.choice(words).strip()) # Generate a random number & Take that word