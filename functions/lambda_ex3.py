# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 12:10:00 2017

@author: abhi
"""

def f(n1):
    return lambda n1:n1+n1

x=f(4)
print(x(4))
        
def f1(n1):
    def f2(n2):
        return n1+n2

x=f1(4)
print(x)