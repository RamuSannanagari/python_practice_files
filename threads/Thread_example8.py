# -*- coding: utf-8 -*-
"""
Created on Sat May 26 22:50:12 2018

@author: abhi
"""


import concurrent.futures

LI = [1,2,3,12,5,6,7,1,5,2]

# Retrieve a single page and report the URL and contents
def square(n):
    return n**2
    
re=[]
# We can use a with statement to ensure threads are cleaned up promptly
with concurrent.futures.ThreadPoolExecutor(max_workers=7) as executor:
    # Start the load operations and mark each future with its URL
    future_to_url = {executor.submit(square, n): n for n in LI}
    print(future_to_url)
    for future in concurrent.futures.as_completed(future_to_url):
        try:
            re.append(future.result())
        except Exception as exc:
            print(' generated an exception' )
            
print(re)
