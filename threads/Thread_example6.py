# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 22:58:58 2017

@author: abhi
"""

import threading
import time
import random

semaphore = threading.Semaphore(0)

def con():
    print("consumer is waiting")
    semaphore.acquire()
    print("consumer item number %s"%item)
    
    
def pro():
    global item
    time.sleep(10)
    for i in range(10000000):
     item=random.randint(0,1000)
    
    print("produced item number %s"%item)
    semaphore.release()
    
    
t1=threading.Thread(target=con)
t2=threading.Thread(target=pro)

t1.start()
t2.start()

t1.join()
t2.join()

print("total  item= ",item)