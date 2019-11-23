# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 08:09:47 2017

@author: abhi
"""

class Interger(object):
    def __init__(self,name):
        self.name = name
    def __get__(self,instance,cls):
        return instance.__dict__[self.name]
    def __set__(self,instance,val):
        if not isinstance(val,int):
            raise AttributeError("Attribute Error")
        instance.__dict__[self.name]=val
                         
class CC:
    x=Interger("x")
    y=Interger("y")
    
    def __init__(self,x,y):
        self.x=x
        self.y=y
        
        
obj=CC(789,20)

print(obj.x,obj.y)
        
obj.x="test"

print(obj.x)