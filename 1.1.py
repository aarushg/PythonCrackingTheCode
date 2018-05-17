#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 18:00:15 2018

@author: aarushg
"""

inString = input("Enter a string:")


def isUnique(testString):
    uniqueList = []
    for x in testString:
         if x not in uniqueList:
                uniqueList.append((x))

    if len(inString) <= len(uniqueList):
        return True
    else:
        return False

print(isUnique(inString))

