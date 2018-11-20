# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 15:47:47 2018

@author: brich
"""

'''
15. Write a Python program to shuffle and print a specified list.


# The shuffle() method randomizes the items of a list in place.
import random
a = ['8','4','9','6','3','12']
print(random.shuffle(a))


16. Write a Python program to generate and print a list of first and 
last 5 elements where the values are square of numbers between 1 and 
30 (both included).


# Nejdrive to umocni vsechny elementy v listu, až pak se z toho vytaha, 
# co treba.

def printValues():
	l = list()
	for i in range(1,21):
		l.append(i**2)
	print(l[:5])
	print(l[-5:])

printValues()



17. Write a Python program to generate and print a list except for the
 first 5 elements, where the values are square of numbers between 1 and
 30 (both included).

def printValues():
	l = list()
	for i in range(1,21):
		l.append(i**2)
	print(l[5:])


printValues()

'''





