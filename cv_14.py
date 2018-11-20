# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 23:15:21 2018

@author: brich
"""
# Count the number of lines in a text file.

def file_lengthy(cv_14):
        with open(cv_14) as f:
                for i, l in enumerate(f):
                        pass
        return i + 1
print("Number of lines in the file: ",file_lengthy("cv_14.txt"))