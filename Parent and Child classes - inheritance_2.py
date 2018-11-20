# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 13:41:34 2018

@author: brich
"""

#Create Vehicle Class  
class Vehicle:      
    
#Constructor for the Parent class
    def __init__ (self, name, color):
        self.name = name
        self.color = color  

#Create Bike Class that inherits Vehicle Class
class Bike(Vehicle):
   #Constructor for the child class      
    def __init__ (self, name, color, price):          
        #Call to Vehicle class Constructor from Bike class          
        Vehicle.__init__ (self, name, color)          
        self.price = price  
        
#Create Vehicle Class Object  
bike = Bike("Honda","Black",25000)  
#Access parent class attributes  
print(bike.name)  
print(bike.color)  
#Access child class attribute  
print(bike.price)

