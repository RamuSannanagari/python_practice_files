# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 18:36:32 2017

@author: abhi
"""
from functools import reduce
L=[1,2,3,4]

#print(list(map(pow,L,[2,2,2,2])))

def f(m,n):
    return m*n

L1=[10,20,30]

L2=[100,200,300]

d={}
c=0
for i in L1:
    d[i]=L2[c]
    c=c+1
    
print(dict(zip(L1,L2)))


#print(L1*L2)

#print(list(lambda l1,l2:l1*l2))

print(list(map(lambda x,y:x*y ,L1,L2)))
print(list(map(f,L1,L2)))

print(reduce(lambda x,y:x+y , [25,50,75]))


print(list(range(-5,5)))

print(list(filter(lambda x:x<0,range(-5,5))))


with open(r"D:\filetest.txt") as fp:
    print(len(list(filter(lambda line: 'python' in line ,fp))))
    
l=list(filter(lambda x : x>1,range(-5,5)))
print(l)