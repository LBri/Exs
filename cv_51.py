# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 16:44:02 2018

@author: brich
"""
'''
69. Write a Python program to remove duplicates from a list of lists. 
'''
old =  [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
# expected = [[10, 20], [30, 56, 25], [33], [40]]
new_set = set(tuple(x) for x in old)
new = [list(x) for x in new_set]
print(new)

'''
70. Write a Python program to get the depth of a dictionary. 
'''
def dict_depth(d):
    if isinstance(d, dict):
        return 1 + (max(map(dict_depth, d.values())) if d else 0)
    return 0
dic = {'a':1, 'b': {'c': {'d': {}}}}
print(dict_depth(dic))
'''
71. Write a Python program to check if all dictionaries in a list 
are empty or not. 
    Sample list : [{},{},{}]
        Return value : True
    Sample list : [{1,2},{},{}]
        Return value : False
'''
my_list = [{},{},{}]
my_list1 = [{1,2},{},{}]
print(all(not d for d in my_list))
print(all(not d for d in my_list1))