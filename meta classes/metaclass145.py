# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 08:20:02 2017

@author: abhi
"""

class BC(type):
    def __new__(met,classname,bases,classdict):
        print("new class created ")
        print(classname,bases,classdict,sep="\n")
        return super().__new__(met,classname,bases,classdict)
    
class Point(metaclass=BC):
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def dis(self):
        return "HELLO"
        
po=Point(1,2)

print(po.dis())

class Newpoint(Point):
    pass

np=Newpoint(4,5)

