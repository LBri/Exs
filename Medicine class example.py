# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 18:25:02 2018

@author: brich
"""
# Python Programming Illustrated for Beginners & Intermediates - W. Sullivan

# Create class 'Medicine'
class Medicine:
    
    # Create 'Medicine' class constructor:
    def __init__(self, name, expiry_year, expiry_month):
        # Initialize instance variables:
        self.name = name
        self.expiry_year = expiry_year
        self.expiry_month = expiry_month
    
    def getExpiryDate(self):
        print('The exp date us: ' + str(self.expiry_month) + '/' + str(self.exexpiry_year

medicine1 = Medicine('x',2020,12)
medicine1.getExpiryDate()
    
