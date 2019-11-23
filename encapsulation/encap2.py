# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 08:16:31 2017

@author: abhi
"""
from functools import wraps


def  logged(func):
     @wraps(func)
     def wrapper(*args,**kwargs):
         print("loggged",func.__name__,args[1:],kwargs)
         return func(*args,**kwargs)
     return wrapper
 
def logmethod(cls):
    for key,value in list(vars(cls).items()):
        #print(key,value)
        if callable(value):
            setattr(cls,key,logged(value))
    return cls
@logmethod
class Ex:
    g=1000
    def spam(self,a,k="v1"):
        print("spam")
    def yellow(self,a):
        print("yell")
        
e=Ex()
print(Ex.__dict__)
e.spam(100,k="v1")
e.yellow(1000)       
        
print(Ex.__dict__)
        
        