#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 23:30:48 2020

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
#use the function within Datasorter1 to get sorted list
K=[]
K=Datasorter1.sort()
print(K)

#plot sorted list
import matplotlib.pyplot as plt
#set basic value for plotting
filename="Task2_sorted_array.png"
plt.xlabel('x')
plt.ylabel('y')
#plot every point in list
for i in K:
    plt.plot(K.index(i),i,'.')
plt.savefig(filename) # write the graph to a file
plt.close()           # close the file
plt.clf()             