# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 13:01:18 2018

@author: abhi
"""

class Ma:
    def display(self):
        print(self.a)
class N(Ma):
    def __init__(self,i):
        self.a=i
        
obj=N(500)
obj.display()