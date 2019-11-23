# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 10:36:21 2017

@author: abhi
"""

def add(num2,num1=10):
    print("num1=",num1)
    print("num2=",num2)
    return num1+num2

def display():
    print("test")
    return

n1=int(input("enter a number :"))
n2=int(input("enter a number :"))

print(add(num1=n1,num2=n2))

print(add(1000,2000))

ee=add(1000)

print(ee)

print('hhkkk ',display())