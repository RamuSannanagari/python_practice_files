# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 21:30:03 2018

@author: abhi
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
print("1")
driver.get("http://www.python.org")

elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
time.sleep(60)

driver.close()
