# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 21:53:35 2018

@author: abhi
"""

import json

fp=open(r"C:\Users\abhi\Documents\PYTHON2\JSON_DATA.json","r")

data=fp.read()
print(type(data))
jsondict=json.loads(data)

print(type(jsondict))
s_c=0
for rec in jsondict:
  if rec[0]['dow'] == 'Thursday':
    print(rec[0]['dow'],rec[1]['time'],rec[2]['conference-categories-count']['Small'])
    s_c=s_c+rec[2]['conference-categories-count']['Small']
#d={'python':3.6}
#jsondict["menu"]["items"].insert(2,d)

#json.dump(jsondict,fp,indent=4)
print(s_c)
fp.close()




