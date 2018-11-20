# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 13:03:10 2018

@author: brich
"""

# generate a password with length "passlen" with no duplicate characters in the password

import string
import random

def pw_gen(size = 8, chars=string.ascii_letters + string.digits + string.punctuation):
	return ''.join(random.choice(chars) for _ in range(size))

print(pw_gen(int(input('How many characters in your password?'))))

#######################################################################################
#import random

#s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
#passlen = 8
#p =  "".join(random.sample(s,passlen ))
#print p