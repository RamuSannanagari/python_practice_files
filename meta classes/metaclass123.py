# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 22:08:00 2017

@author: abhi
"""

class MetaTwo(type):
    def __new__(met, classname, supe, classdic):
        print('In MetaTwo.new: ', classname, supe, classdic, sep='\n...')
        return type.__new__(met, classname, supe, classdic)
    def __init__(Clas, classname, supe, classdict):
        print('In MetaTwo.init:', classname, supe, classdict, sep='\n...')
        print('...init class object:', list(Clas.__dict__.keys()))
class Eggs:
    pass
print('making class')

class Spam(Eggs, metaclass=MetaTwo): # Inherits from Eggs, instance of MetaTwo
          data = 1 # Class data attribute
          def meth(self, arg): # Class method attribute
            return self.data + arg
print('making instance')
X = Spam()
print('data:', X.data, X.meth(2))