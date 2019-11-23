# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 15:30:47 2017

@author: abhi
"""

import csv

fp=csv.reader(open(r"C:\Users\abhi\Downloads\FL_insurance_sample.csv\FL_insurance_sample.csv"))

for rec in fp:
    #li=rec.split(sep=",")
    print(rec[0],rec[2])
    
#print(help(csv.)