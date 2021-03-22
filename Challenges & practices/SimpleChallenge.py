# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 14:10:38 2020

@author: MR.COOL
"""

def LeftSkew(num):
    print("Left Skewed Triangle")
    for i in range(num):
        for j in range(i+1):
            print("*",end="")
        print()
        
def RightSkew(num):
   print("Right Skewed Triangle")
   for i in range(num,0,-1):
       for j in range(1,i+1):
         print("*",end="")
       print()  
   

def Triangle(num):
    print("Triangle")
    for i in range(num):
        for j in range(num-i):
            print (" ",end="")
        for j in range(2*i+1):
            print("*",end="")
        print()
        
def invertedTriangle(num):
    print("Inverted Triangle")
    for i in range(num,0,-1):
        for j in range(num-i):
            print (" ",end="")
        for j in range(2*i-1):
            print ("*",end="")
        print()

LeftSkew(5)
print()
RightSkew(5)
print()
invertedTriangle(5)
print()    
Triangle(5)    

