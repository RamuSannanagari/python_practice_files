# -*- coding: utf-8 -*-
"""
Created on Sat Jul 21 22:21:52 2018

@author: abhi
"""
import re
line = 'asdf fjdk; afed, fjek,asdf, foo'
print(re.split(r'[;,\s]\s*', line))