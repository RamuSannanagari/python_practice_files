# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 22:21:05 2017

@author: abhi
"""

import threading as t

gv =0
COUNT=100000

shared_resource_lock=t.Lock()

def inc():
    global gv
    for i in range(COUNT):
        shared_resource_lock.acquire()
        gv=gv+1
        shared_resource_lock.release()
        
 
def dec():
    global gv
    for i in range(COUNT):
        shared_resource_lock.acquire()
        gv=gv-1
        shared_resource_lock.release()       
        
        
t1=t.Thread(target=inc)
t2=t.Thread(target=dec)

t1.start()

t2.start()

t1.join()

t2.join()

print("gv =" ,gv)