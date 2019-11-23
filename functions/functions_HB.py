# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 11:16:23 2017

@author: abhi
"""

def f1(n):
    def f2(m):
        return m*n
    return f2

x=f1(4)

print(x(5))

su=0
def f(L):
    global su
    for i in L:
        print(i)
        if not isinstance(i,int):
            f(i)
            print(i)
            print('list sum=',su)
        else:
            su+=i
            print('int sum=',su)
    return su

l=[1,2,[3,4],5,6,7,8,[9,10,11]]

print(f(l))

print(sum([1,2,3,4,5,6,7,8,9,10,11]))

def gf(n):
    while n>0:
        yield n
        n=n+1
        
g=gf(1)

print([next(g) for _ in range(10)])
print([next(g) for _ in range(10)])