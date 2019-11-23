# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 22:35:08 2017

@author: abhi
"""

import threading

import time

class Box(object):
    lock=threading.RLock()
    def __init__(self):
        self.total_items=0
        
    def execute(self,n):
        Box.lock.acquire()
        self.total_items+=n
        Box.lock.release()
        
    def add(self):
        Box.lock.acquire()
        self.execute(1)
        Box.lock.release()
        
    def remove(self):
        Box.lock.acquire()
        self.execute(-1)
        Box.lock.release()
        
        
def adder(box,items):
    while items > 0:
        print("adding 1 item in box : ",items)
        box.add()
        time.sleep(5)
        items=items-1
        
def remover(box,items):
    while items > 0:
        print("removing 1 item in box: ",items)
        box.remove()
        time.sleep(5)
        items=items-1
        
items=5

box=Box()

t1=threading.Thread(target=adder,args=(box,items,))
t2=threading.Thread(target=remover,args=(box,items,))

t1.start()
t2.start()

t1.join()
t2.join()

print("total  items ",box.total_items)