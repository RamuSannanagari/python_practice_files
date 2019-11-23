# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 09:00:03 2017

@author: abhi
"""

from functools import reduce

add=lambda x,y:x+y

L=[2,4,6]

print(add(4,5))

j=0
for i in L:
    L[j]=i**2
    j+=1
    
print(L)

M=[2,4,6]

sq=lambda x: x**2
print(tuple(map(sq,M)))


print(sq(100))

M2=[1,2,3,4,5,6,7,8,9,10]

even_f=lambda x: x%2==1

print(even_f(10))

print(list(filter(even_f,M2)))


mul=lambda x,y:x*y

M5=[1,3]


print(reduce(mul,[1,4],[4,5]))



















