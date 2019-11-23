# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 06:17:14 2017

@author: abhi
"""

def ge(n=0):
    while True:
        n=n+1
        yield n
go=ge()
print([next(go) for _ in range(10)])
print([next(go) for _ in range(10)])