# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 22:12:10 2018

@author: brich
"""
'''
57. Write a Python program to check if all items of a list is equal to a given string. 

listik = ['Bohumir','Martin','Vanda']
string = 'Marie'

for x in listik:
    if x == string:
        print('Equal')
    else:
        print(x, 'is not equal to', string)
####### 2nd method: ##########
color1 = ["green", "orange", "black", "white"]
color2 = ["green", "green", "green", "green"]

print(all(c == 'blue' for c in color1))
print(all(c == 'green' for c in color2))

58. Write a Python program to replace the last element in a list with another list. 
    Sample data : [1, 3, 5, 7, 9, 10], [2, 4, 6, 8]
    Expected Output: [1, 3, 5, 7, 9, 2, 4, 6, 8]

'''
sample = [1, 3, 5, 7, 9, 10]
add = [2, 4, 6, 8]
sample[-1:] = add
print(sample)


'''
59. Write a Python program to check if the n-th element exists in a given list. 
'''
x = [1, 2, 3, 4, 5, 6]
xlen = len(x)-1 #i.e. 6-1 = 5
print(x[xlen]) # na pátém místě je šestka