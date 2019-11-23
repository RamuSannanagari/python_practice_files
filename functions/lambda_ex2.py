# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 11:48:43 2017

@author: abhi
"""
from functools import reduce

l=[1,2,3,4]

ll=list(map(lambda x:x*x,l))

print(ll)

lll=list(filter(lambda x:x%2!=0,l))

print(lll)

l1=[1,2,4,5]
l2=[4,5,6]

llll=list(map(lambda x,y:x+y,l1,l2))

lllll=reduce(lambda x,y:x+y,l1)

print(lllll)

