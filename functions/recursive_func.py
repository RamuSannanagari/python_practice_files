# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 08:25:18 2018

@author: abhi
"""

def f(n):
    if n==1:
        return 1
    else:
        return n*f(n-1)
    
print(f(4))