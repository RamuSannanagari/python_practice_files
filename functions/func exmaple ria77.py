# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 21:40:48 2017

@author: abhi
"""

def MA():
   l=[]
   for i in range(5):
      l.append(lambda x:i**x)
   return l

a=MA()

print(a[1](2))
