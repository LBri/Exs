# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 18:48:12 2018

@author: brich
"""

'''
49. Write a Python program to convert list to list of dictionaries. 
    Sample lists: ["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", 
    "#800000", "#FFFF00"]
    Expected Output: [{'color_name': 'Black', 'color_code': '#000000'}, 
    {'color_name': 'Red', 'color_code': '#FF0000'}, {'color_name': 'Maroon',
    'color_code': '#800000'}, {'color_name': 'Yellow', 'color_code': '#FFFF00'}]

keys = ["Black", "Red", "Maroon", "Yellow"]
values = ["#000000", "#FF0000", "#800000", "#FFFF00"]

print(dict(zip(keys,values)))


50. Write a Python program to sort a list of nested dictionaries.
'''

listik = [{'key': {'subkey': 19}},{'key': {'subkey': 20}},{'key': {'subkey': 12}},
{'key': {'subkey': 32}}]
listik.sort(key=lambda e: e['key']['subkey'], reverse=False)
print(listik)

