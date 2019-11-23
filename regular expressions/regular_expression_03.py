# -*- coding: utf-8 -*-
"""
Created on Sat Jul 21 22:18:33 2018

@author: abhi
"""

import re

phone = "2004-959-559 # This is Phone Number"

# Delete Python-style comments
num = re.sub(r'#.*$', "", phone)
print ("Phone Num : ", num)

# Remove anything other than digits
num = re.sub(r'\D', "", phone)    
print ("Phone Num : ", num)