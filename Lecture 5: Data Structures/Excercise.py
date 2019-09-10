#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 16:30:27 2019

@author: artlist
"""

#Write a program find the most repeated character in this text
sentence = "Thia is a common interview question"
def getNumberRepeat(x, sentence):
    num = 0
    for _ in list(sentence):
        if _ == x:
            num += 1
    return num
uniqueChars = list(set(c for c in list(sentence) if c != " "))
countDict = {char: getNumberRepeat(char,sentence) for char in uniqueChars }
print(max(countDict, key = countDict.get)) 
