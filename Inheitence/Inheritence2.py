# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 10:39:04 2018

@author: abhi
"""

class Parent:
    P_V=1000
    def parent_m(self):
        print("parent_m = ",self.P_V)
        self.child_m()
    def child_m(self):
        print("child_m in parent = ",self.C_V)       
        
class Child(Parent):
    C_V=2000
    def child_m(self):
        print("child_m = ",self.C_V)   
        
c_obj=Child()

c_obj2=Child()

c_obj.parent_m()

c_obj2.child_m()