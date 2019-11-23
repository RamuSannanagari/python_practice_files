# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 18:48:28 2018

@author: abhi
"""
import sys



class Numericvalid(Exception):
    def __str__(self):
        return "Please enter Values greater than 100"
    
try:
    n1=input("Enter a N1 number : ")
    n2=input("Enter a N2 number : ")
    if int(n1) < 100 or int(n2) < 100:
        raise Numericvalid(n1,n2)
    print(int(n1)+int(n2))
except (ValueError,TypeError):
    print("please enter N1 and N2 as Numeric val")
    #raise
except Numericvalid as e:
    print(e,e.args)
except:
    print("please enter Numeric Inputs only")

    
finally:
    print("END OF THE PROGRAM")
    