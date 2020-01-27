#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 17:15:34 2020

@author: s1914361
"""
import numpy as np
#creat a list of random number
numb=[]
numb=random_integers(100,30)
print(numb)
#creat a class
class Datasorter(object):
#give the class a initial value for inputting  
    def __init__(self,somedata):
        self.x=somedata
#achieve the sorting function        
    def sort(self):
        L=list()
        for i in range(len(self.x)):
            m=np.min(self.x)
            L.append(m)
            self.x.remove(m)
        return L
#give a example: put initial value into class         
Datasorter1=Datasorter(numb)
#use the function within Datasorter1
print(Datasorter1.sort())


