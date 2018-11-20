# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 16:25:51 2018

@author: brich
"""
'''
40. Write a Python program to split a list based on first character of word. 

from itertools import groupby
from operator import itemgetter

word_list = ['be','have','do','say','get','make','go','know','take','see','come','think',
     'look','want','give','use','find','tell','ask','work','seem','feel','leave','call']

for letter, words in groupby(sorted(word_list), key=itemgetter(0)): # the key for sorting is the first character in the element
    print(letter) # print the key
    for word in words: # then print the words that belong it
        print(word)
        

41. Write a Python program to create multiple lists. 
'''

obj = {} # empty dictionary
for i in range(1, 11): # set the number of lists to be created
    obj[str(i)] = [] # create empty lists in the 'obj' distionary 
print(obj)