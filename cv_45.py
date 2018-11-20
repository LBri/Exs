# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 20:48:15 2018

@author: brich
"""

'''
54. Write a Python program to concatenate elements of a list. 

color = ['red', 'green', 'orange']
print('-'.join(color)) # result: red-green-orange     
print(''.join(color)) # result: redgreenorange 


55. Write a Python program to remove key values pairs from a list of dictionaries. 

'''
old_dict = {'key1': 123, 'key2': 321},{'key1':987, 'key2':456}

new_list = [{k: v for k, v in d.items() if k != 'key1'} for d in old_dict]

print(new_list)

'''
56. Write a Python program to convert a string to a list.
'''

string = ('Jahody')
print(list(string))


