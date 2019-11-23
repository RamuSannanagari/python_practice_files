# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 23:34:19 2017

@author: abhi
"""

import threading
import time

def f_f():
    print(threading.currentThread().getName()+" Starting \n")
    time.sleep(2)
    print(threading.currentThread().getName()+" Exiting  \n")
    return
def f_s():
    print(threading.currentThread().getName()+" Starting \n")
    time.sleep(2)
    print(threading.currentThread().getName()+" Exiting  \n")
    return
def f_t():
    print(threading.currentThread().getName()+" Starting \n")
    time.sleep(2)
    print(threading.currentThread().getName()+" Exiting  \n")
    return

t1=threading.Thread(name="f_f",target=f_f)
t2=threading.Thread(name="f_s",target=f_s)
t3=threading.Thread(name="f_t",target=f_t)
 
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()