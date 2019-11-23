# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 09:33:45 2017

@author: abhi
"""

class Typed(object):
    expected_type = object
    def __init__(self,name=None):
        self.name = name
    def __get__(self,instance,cls):
        return instance.__dict__[self.name]
    def __set__(self,instance,value):
        if not isinstance(value,self.expected_type):
            raise AttributeError("invalid number")
        print(' self.name =',self.name)
        instance.__dict__[self.name]=value
                    
class Number(Typed):
    expected_type=int
    
def typed(cls):
    print('---------------')
    print(vars(cls))
    print('---------------')
    for key,value in vars(cls).items():
        if isinstance(value,Typed):
            value.name=key
            print("typed=", value.name)
    return cls


class st(type):
      def __new__(meta,name,bases,methods):
          cls=super().__new__(meta,name,bases,methods)
          cls=typed(cls)           
          return cls


class Ex(metaclass=st):
    i=Number()
    def __init__(self,i):
        self.i=i
e1=Ex(100)

print(e1.i)
