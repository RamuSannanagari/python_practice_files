# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 11:21:01 2017

@author: abhi
"""

import json

fp=open(r"file_data.json")

s=json.loads(fp.read())

print(type(s))
print(s['widget']['text'])

'''

#print(fp.readline())

for rec in fp:
    s=json.loads(rec)
    print(s['countryshortname'])
    if s['countryshortname'] == 'China':
        print("%s --> %s"%(s['idacommamt'],s['id']))
'''