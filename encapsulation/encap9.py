# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 11:35:10 2018

@author: abhi
"""

class Ex:
    g=1000
    def spam(self,a):
        print("spam called ",a)
        print("spam")
    def yell(self,a,b):
        print("yell called ",a,b)
        print("yell")
        
e=Ex()

e.spam(100)
e.yell(1000,b=2000)
        