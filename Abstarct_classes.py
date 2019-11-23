# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 06:33:41 2017

@author: abhi
"""

from abc import ABCMeta,abstractmethod

class A(metaclass=ABCMeta):
    @abstractmethod
    def display(self):
        pass
    def dispkay2(self):
        pass
    
class B(A):
    def display2(self):
        return "DISPALYED"
        
b1=B()

print(b1.display())