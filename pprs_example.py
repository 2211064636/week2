#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 17:09:03 2020

@author: s1914361
"""

class testClass():
  '''
  This is a class to illustrate
  how classes work
  '''
  # This function is called when the class is first applied
  # it initialises the class
  def __init__(self,somedata,moredata):  # we pass two items to store in the class
    '''The class initialiser'''
    self.x=somedata  # here "self" is the instance of the clasa.s The "." means there is something inside that class
    self.y=moredata  # in this case, we have saved two pieces of data, x and y. We have already used the "." when using numpy etc.
  # a function we would like to use. "Self" contains the data
  def multiplyContents(self):
    '''Function to multiply the contents together'''
    z=self.x*self.y   # note that z is not in self, so is not saved after this function
    print("The multiplitcation of",self.x,"and",self.y,"is",z)



# call an instance of that class
class1=testClass(3,4)   # this calls __init__ and passes 3 and 4 to be saved as x and y

# call the function
class1.multiplyContents()

# we can directly access the data too
print("Data within is",class1.x,class1.y)

# We can create a separate instance of the class, which will be independent from class1
class2=testClass(10,42)   # this calls __init__ and passes 3 and 4 to be saved as x and y


# to prove they are independent
class1.multiplyContents()
class2.multiplyContents()