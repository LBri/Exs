# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 16:25:38 2018

@author: brich
"""
'''
38. Write a Python program to change the position of every n-th value 
    with the (n+1)th in a list. 
    Sample list: [0,1,2,3,4,5]
    Expected Output: [1, 0, 3, 2, 5, 4]


from itertools import zip_longest, chain, tee
# itertools = functions creating iterators for efficient looping
sample = [0,1,2,3,4,5]

def change(sample):
    sample, out = tee(iter(sample),2) # splits iterator (the 'sample') into two
    return list(chain.from_iterable(zip_longest(sample[1::2], sample[::2])))

print(change(sample))


def from_iterable(iterables):
    # chain.from_iterable(['ABC', 'DEF']) --> A B C D E F
    for it in iterables:
        for element in it:
            yield element
'''

'''
39. Write a Python program to convert a list of multiple integers into
    a single integer. 
    Sample list: [11, 33, 50]
    Expected Output: 113350
'''
sample = [11, 33, 50]
x = int("".join(map(str, sample)))
print(x)

#from itertools import chain
#sample = [11, 33, 50]
#print(chain(sample))