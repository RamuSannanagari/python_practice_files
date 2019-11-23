# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 08:50:23 2017

@author: abhi
"""

class A:
    def d(self):
        print("display A")
        
class B(A):
    pass

class C:
    def d(self):
        print("display C")
        #super().d()
        
class D(B,C):
    pass

o=D()

o.d()