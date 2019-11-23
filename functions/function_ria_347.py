# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 22:27:47 2017

@author: abhi
"""

def f():
    l=[]
    for i in range(5):
        l.append(lambda x,i=i:i**x)
    return l

a=f()

print(a[0](0),a[1](1),a[2](2),a[3](2))