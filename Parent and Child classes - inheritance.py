# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 13:34:25 2018

@author: brich
"""

class Parent:
    name = ''
    age = ''
    def methodA(self):
        print('Hello, I am a Parent class method.')

# Create a class Child that inherits Parent:
class Child(Parent):
    def methodB(self):
        print('Hello, I am a Child class method.')
        
# Create object of class Child
child = Child()

# Access Parent class method
child.methodA()

# Access Child class method
child.methodB()

# Access parent class attributes 
child.name = 'Jacob'
child.age = 10
print(child.name + ' ' + str(child.age))

