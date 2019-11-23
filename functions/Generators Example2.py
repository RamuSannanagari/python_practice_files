# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 06:25:06 2017

@author: abhi
"""

def gen():
    for i in range(10):
       X = yield i
       print(X)
    
G =gen()

#print(next(G))    

#G.send(78)

#G.send(88)


print(next(G))    
print(next(G))    
print(next(G))    