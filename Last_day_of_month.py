# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 20:26:50 2018

@author: brich
"""

import datetime as dt

dat = dt.date(2000,2,1)

def last_day(dat):
    yr = dat.year
    mon = dat.month
        
    long = [1,3,5,7,8,10,12]
    short = [4,6,9,11]

    if mon in long:
        dat = dt.date(yr,mon,31)
    elif mon in short:
        dat = dt.date(yr,mon,30)
    else:
        if yr % 4 == 0 and yr % 100 != 0 or yr % 400 ==0:
            dat = dt.date(yr,mon,29)
        else:
            dat = dt.date(yr,mon,28)
    return(dat)
print(last_day(dat))