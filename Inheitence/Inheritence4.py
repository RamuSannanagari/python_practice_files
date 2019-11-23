# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 11:12:44 2018

@author: abhi
"""

class parent0:
    def child_m(self):
        print("child_m in parent0 = ",self.C_V)   
class Parent1(parent0):
    P_V=1000
    def child_m(self):
        print("child_m in parent1 = ",self.C_V)   
        super().child_m()
class Parent2(Parent1):
    #cobj3=parent0()
    #cobj3.child_m()
    def child_m(self):
        print("child_m in parent2 = ",self.C_V)  
        super().child_m()


class Child(Parent2):
    C_V=2000
    
c_obj=Child()

c_obj.child_m()

