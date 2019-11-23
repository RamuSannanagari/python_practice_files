# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 22:00:26 2017

@author: abhi
"""

def met(self,arg):
    return (self.data+arg)*10


class MetaOne(type):
    def __new__(meta, classname, supers, classdict):
        #print('In MetaOne.new:', meta, classname, supers, classdict, sep='\n...')
        classdict['meth2']=met
        return type.__new__(meta, classname, supers, classdict)
    
class Eggs:
    pass

print('making class')


class Spam(Eggs, metaclass=MetaOne): # Inherits from Eggs, instance of MetaOne
  data = 1 # Class data attribute
  def meth(self, arg): # Class method attribute
   return self.data + arg


class spam2(Spam):
  data2 = 11 # Class data attribute
  def meth2(self, arg): # Class method attribute
   return self.data + arg    


#print('making instance')
X = spam2()
print('data:', X.data2, X.meth2(2))