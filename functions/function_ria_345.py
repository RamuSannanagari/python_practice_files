# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 22:56:58 2017

@author: abhi
"""

def f1(a,b):
    a=20
    b[0]=12
    print(b)
	
a=30
l=[1,2]
f1(a,l[:])
print(l)