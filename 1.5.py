#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 15 01:55:21 2018

@author: aarushg


one away


 One Away: There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. Given two strings, write a function to check if they are
one edit (or zero edits) away.
EXAMPLE
pale, pIe -> true
pales. pale -> true
pale. bale -> true
pale. bake -> false 











import itertools 
 
num = [1, 2, 3]
color = ['red', 'while', 'black']
value = [255, 256]
 
# iterates over 3 lists and excutes 
# 2 times as len(value)= 2 which is the
# minimum among all the three 
for (a, b, c) in zip(num, color, value):
     print a, b, c
 
print "\niterating using izip"
for (a, b, c) in itertools.izip(num, color, value):
    print a, b, c





"""





from difflib import SequenceMatcher

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


fString = input("Enter first string:")
sString = input("Enter second string:")

fStringSort = sorted(fString.lower())

sStringSort = sorted(sString.lower())

#print(fStringSort)
#print(sStringSort)



if similar(fStringSort, sStringSort) > .5:
    
    print(True)
    
else:
    
    print(False)

