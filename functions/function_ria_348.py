# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 22:35:04 2017

@author: abhi
"""

def f(a,*b,**c):
    print(a,b,c)
    
    
f(1,2,3,c=9,d=100)