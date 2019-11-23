# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 23:26:05 2017

@author: abhi
"""

import threading

th=[]

def f(i):
    print("%d = thread"%(i))
    
    
for i in range(5):
    t=threading.Thread(name=i,target=f,args=(i,))
    th.append(i)
    t.start()
    t.join()
    
    
print(th)