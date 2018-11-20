# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 18:55:51 2018

@author: brich
"""

### The __add__ method ###

# Create class Person:
class Person:
    # Create method with instance attributes:
    def __init__(self,age):
        # initialize instance variable
        self.age = age
    # Overriding __add__ special method:
    def __add__(self,other):
        return self.age + other.age
    # When the two objects of the Person class are added via 
    # the “+” operator, actually the values for the age 
    # attributes of the objects will be added.
### The __gt__ method ###
    def __gt__(self,other):
        return self.age > other.age
### The __str__ method ###
    def __str___(self,):
        return 'The person is' + self.name
p1 = Person("James")
print(str(p1))