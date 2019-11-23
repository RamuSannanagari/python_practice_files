# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 08:57:33 2018

@author: abhi
"""

import collections as c

d=c.OrderedDict()
d={110:'a',102:'b',104:'d',103:'c'}

#d4=c.OrderedDict(sorted(d.items(),key=lambda t:t[1]))
d4=c.OrderedDict(sorted(d.items(),key=lambda t:t[1]))
print(d4)

d2={101:'a',102:'b',104:'d',103:'c'}

for k,v in d.items():
    print(k,v)
    
for k,v in d2.items():
    print(k,v)


L=[('a',1),('b',1),('a',2)]  
    
d3=c.defaultdict()

print(d3)
