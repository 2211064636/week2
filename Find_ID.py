#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 01:54:32 2020

@author: s1914361
"""
import numpy
import math
def id_generator(size=6,chars=str.ascii.uppercase+string.digits):
    return ''.join(random.choice(chars) for x in range(size))

longl=[]
for i in range(num):
    long1.append(id_generator())
    print(long1[p])

n=random.randint(0,num)

n=random.randiant(0,num)
print"search for" + long1[n]

found=binarySearch(long1[n],long1)
if (found==-1):
    print("string not found")
else:
    print("string found at position:"+str(found)