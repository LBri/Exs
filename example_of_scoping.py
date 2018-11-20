# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 16:59:42 2018

@author: brich
"""

###### Example demonstrating how to reference the different scopes and namespaces,
###### and how global and nonlocal affect variable binding:
def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)

# Note how the local assignment (which is default) didn’t change scope_test’s binding of spam.
# The nonlocal assignment changed scope_test’s binding of spam, and the global assignment changed
# the module-level binding.
# You can also see that there was no previous binding for spam before the global assignment.