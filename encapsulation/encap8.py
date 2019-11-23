# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 11:53:44 2018

@author: abhi
"""

class Person:
    cl=1000
    def __init__(self,id,name):
        self.id=id
        self.name=name
    def __repr__(self):
        return "sample object in Person class"
    def __str__(self):
        return "sample object for sales cals"

vinod=Person(101,"vinod kumar")
y=Person("test",101)

#print(repr(y))
#print(y)
print(y.__dict__)

