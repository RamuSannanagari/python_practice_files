# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 23:10:02 2017

@author: abhi
"""

from bs4 import BeautifulSoup

import urllib


fp=urllib.request.urlopen("https://analytics.usa.gov/")

data=fp.read()

soup=BeautifulSoup(data,"lxml")

print(soup.title.name)
print(soup.title.string)

for  link  in  soup.find_all("a"):
    print(link["href"])