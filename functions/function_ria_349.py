# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 11:00:28 2017

@author: abhi
"""

LI=[1,2,3]
t=(1,2,3)
s1={1,2,3}
s2={'k1':'v1'}

def str_f(name):
    #name=(4,5,6)
    name['k1']='v22'
    print(name)
    
str_f(s2)

print(s2)

def f(a,*b,**c):
    print(a,b,c)
    
f(1,2,name="python")