# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 11:01:04 2018

@author: abhi
"""
class parent0:
    pass
class Parent1(parent0):
    P_V=1000
    def child_m(self):
        print("child_m in parent1 = ",self.C_V)       
class Parent2:
    P_V=1000
    def parent_m(self):
        print("parent_m = ",self.P_V)
        self.child_m()
    def child_m(self):
        print("child_m in parent2 = ",self.C_V)  
    def super_m(self):
        print('super_m method in parent2')
        
class Child(Parent1,Parent2):
    C_V=2000

c_obj=Child()

c_obj.super_m()

