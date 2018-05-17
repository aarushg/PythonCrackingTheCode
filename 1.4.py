# -*- coding: utf-8 -*-
"""
Created on Sun May 13 01:38:56 2018

@author: Aarush Gupta
"""
#https://docs.python.org/2/library/collections.html
#https://pymotw.com/2/collections/counter.html


from collections import Counter
import time

def isPermutationOfPalindrome(string):

    counter = Counter(string)

    oddCount=0

    for c in counter:

        if not c.isalnum():
            continue

        if counter[c] % 2 == 1:
            oddCount += 1

        if oddCount > 1:
            return False


    return True


inString = input("Enter a string:")


print(isPermutationOfPalindrome(inString))


time.sleep(100) 