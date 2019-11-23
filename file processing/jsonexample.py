# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 12:13:23 2017

@author: abhi
"""

import json

fp=open(r"C:\Users\abhi\Documents\PYTHON2\example.json")

s2=fp.read()

d=json.load(fp)

print(type(d))

#print(d["menu"][ "popup"]["menuitem"][0]['value'])

for di in d["menu"][ "popup"]["menuitem"]:
    print(di['value'])
    
    
    
'''
fp=open(r"C:\Users\abhi\Documents\PYTHON2\JSON_DATA.json","w")
jsondata=json.dumps(jsondict)
'''
'''
for v in jsondict["menu"]["items"]:
    if isinstance(v,dict):
        if "label" in v.keys():
            print(v["label"])

fp.close()
'''