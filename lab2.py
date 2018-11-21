# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 09:50:34 2018

@author: BIT
"""

import numpy as np
import matplotlib.pyplot as plt

def gamma(x,a,b):
    if x<a :
        return 0
    elif x>=b :
        return 1
    else : 
        return (x-a)/(b-a)
    
def s(x,a,b,y):
    if x<a :
        return 0
    elif x>=a and x<b :
        return 2*(np.power((x-a)/(y-a),2))
    elif x>=b and x<y : 
        return 1-2*(np.power((x-y)/(y-a),2))
    else :
        return 1

def l(x,a,b):
    if x<a :
        return 1
    elif x>=a and x<b :
        return (b-x)/(b-a)
    else : 
        return 0

def tri(x,a,b,y):
    if x<=a :
        return 0
    elif x>a and x<=b :
        return (x-a)/(b-a)
    elif x>b and x<=y : 
        return (y-x)/(y-b)
    else :
        return 0    

def trap(x,a,b,c,d):
    if x<=a :
        return 0
    elif x>a and x<=b :
        return (x-a)/(b-a)
    elif x>b and x<=c : 
        return 1
    elif x>c and x<=d :
        return (d-x)/(d-c)
    else :
        return 0 

def gauss(x,b,c):
    return np.exp(-1/2*(np.power((x-c)/(b),2)))

def bell(x,a,b,c):
    return 1/(1+np.power(np.abs((x-c)/(a)),2*b))
    

t1=np.arange(0,30,0.01)
arr=[]
for x in t1 :
    arr.append(gamma(x,10,20))
plt.title("Gamma Function")
plt.xlabel("x")
plt.ylabel("Gamma(x)")
plt.grid()
plt.plot(t1,arr)
plt.show()

t1=np.arange(-10,10,0.01)
arr=[]
for x in t1 :
    arr.append(s(x,0,1,2))
plt.title("S Function")
plt.xlabel("x")
plt.ylabel("S(x)")
plt.grid()
plt.plot(t1,arr)
plt.show()

t1=np.arange(-5,50,0.01)
arr=[]
for x in t1 :
    arr.append(l(x,10,20))
plt.title("L Function")
plt.xlabel("x")
plt.ylabel("L(x)")
plt.grid()
plt.plot(t1,arr)
plt.show()

t1=np.arange(-5,50,0.01)
arr=[]
for x in t1 :
    arr.append(tri(x,10,20,30))
plt.title("Triangular Function")
plt.xlabel("x")
plt.ylabel("Triangular(x)")
plt.grid()
plt.plot(t1,arr)
plt.show()

t1=np.arange(-5,50,0.01)
arr=[]
for x in t1 :
    arr.append(trap(x,10,20,30,40))
plt.title("Trapezoidal Function")
plt.xlabel("x")
plt.ylabel("Trapezoidal(x)")
plt.grid()
plt.plot(t1,arr)
plt.show()

t1=np.arange(-5,50,0.01)
arr=[]
for x in t1 :
    arr.append(gauss(x,10,20))
plt.title("Gaussian Function")
plt.xlabel("x")
plt.ylabel("Gaussian(x)")
plt.grid()
plt.plot(t1,arr)
plt.show()

t1=np.arange(-5,50,0.01)
arr=[]
for x in t1 :
    arr.append(bell(x,10,20,30))
plt.title("Bell Function")
plt.xlabel("x")
plt.ylabel("Bell(x)")
plt.grid()
plt.plot(t1,arr)
plt.show()