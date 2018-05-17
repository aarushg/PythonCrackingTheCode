# -*- coding: utf-8 -*-
"""
Created on Sat May 12 21:25:25 2018

@author: Aarush Gupta

replace all space in the string with %20
"""


import time

import re

String , length = input("Enter string:") , input("Enter length:")
stringlength = len(String)


if " " in String:
    spaceremove = re.sub(' +',' ',String)
    newstring = spaceremove.replace(" ", "%20")
    lenofnewstring = len(newstring)
    lenofnewstringminus = lenofnewstring - 3
    print(newstring[:int(lenofnewstringminus)])
else:
    print(String)


time.sleep(100) 
