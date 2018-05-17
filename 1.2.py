# -*- coding: utf-8 -*-
"""
Created on Sat May 12 19:10:48 2018

@author: Aarush Gupta

One string is a permuation of the other.
"""
    

fString = input("Enter first string:")
sString = input("Enter second string:")

lenfString = len(fString)
lensString = len(sString)

listfString = list(fString)
listsString = list(sString) 

if lenfString != lensString:
    print("Invalid:Strings have to be the same length")
else:
    #sorts1 = listfString.sort()
    #sorts2 = listsString.sort()
    
    sorts1 = sorted(listfString)
    sorts2 = sorted(listsString)
    
    if sorts1 == sorts2:
      print("The first string is a permutation of the other.")
    else:
      print("The string is not a permutation.")