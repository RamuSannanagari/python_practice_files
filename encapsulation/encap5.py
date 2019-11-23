# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 08:43:23 2017

@author: abhi
"""

'''
class M:
    def __setattr__(self,name,value):
        self.__dict__[name]=value
'''
class En:
    def __init__(self,p,t,r):
        self.p=p
        self.t=t
        self.r=r 
    def __getattr__(self,name):
          return " invalid value = {}".format(name)
    def __setattr__(self,name,value):
        if name not in {'p','r','t','a'}:
            raise AttributeError("attribute error invalid attribute")
        #super().__setattr__(name,value)
        self.__dict__[name]=value        
      
e=En(100,20,30)
                   
print(e.p)
print(e.t)
#print(e.ttt)
e.p=1000
#print(e.yyyy)
print(e.__dict__)
e.a=1000