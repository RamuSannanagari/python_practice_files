# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 22:20:30 2017

@author: abhi
"""

class En:
    def __init__(self,p,t,r):
        self.p=p
        self.t=t
        self.r=r
        
    @property    
    def r(self):
        return self._price
    
    @r.setter
    def r(self,newprice):
        if not isinstance(newprice,float):
            raise TypeError("invalid number ,please enter numeric value")
        self._price=newprice
            
    def display(self):
        print("display method")
    
    @property    
    def intrest(self):
        return round((self.p*self.r*self.t)/100)
    
    @intrest.setter
    def intrest(self,newint):
        self.r=float(round(newint*100/self.p*self.t))    
    def __repr__(self):
        return 'EN({!r} {!r} {!r})'.format(self.p,self.t,self.r)
        
        
        
o=En(1000000,1,8.9)

#print(o.intrest)
#print(o.r)
#o.intrest=6000
#print(o.r)


#print(o.__dict__)
#print(En.__dict__)