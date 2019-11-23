# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 23:48:34 2017

@author: abhi
"""

import threading
import time

exited_flag=0

class TC(threading.Thread):
    def __init__(self,t_id,name,cnt):
        threading.Thread.__init__(self)
        self.t_id=t_id
        self.name=name
        self.cnt=cnt
        
    def run(self):
        print(threading.currentThread().getName()+" Starting \n")
        print_name(self.name,self.cnt,5)
        print(threading.currentThread().getName()+" Exiting  \n")
        
def print_name(tname,delay,cnt):
    while cnt:
        if exited_flag:
            thread.exit()
        time.sleep(delay)
        print("%s %s \n"%(tname,time.ctime(time.time())))
        cnt-=1
        
t1=TC(11,'T-1',1)
t2=TC(12,'T-2',2)

t1.start()
t2.start()

t1.join()
t2.join()

print("Exiting main thread")