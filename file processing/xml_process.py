# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 11:18:50 2017

@author: abhi
"""
from bs4 import BeautifulSoup
fp=open("country_d.xml")

xml_data=fp.read()

soup=BeautifulSoup(xml_data,"lxml")

for rec in soup.find_all("dist"):
    print(rec["name"],rec.population.string,rec.ocupation.string)
