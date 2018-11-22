# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 11:04:05 2018

1 2 3

0.2 0.5 1

1 2

0.3 0.9

1

0.1
@author: BIT
"""
import numpy as np

    
s= input()
Xnum = list(map(int, s.split()))
s= input()
Xval = list(map(float, s.split()))
X = {}
for x in range(len(Xnum)):
    X[Xnum[x]]=Xval[x]

s= input()
Ynum = list(map(int, s.split()))
s= input()
Yval = list(map(float, s.split()))
Y = {}

for x in range(len(Ynum)):
    Y[Ynum[x]]=Yval[x]

s= input()
Znum = list(map(int, s.split()))
s= input()
Zval = list(map(float, s.split()))
Z = {}

for x in range(len(Znum)):
    Z[Znum[x]]=Zval[x]

print("\n")

XY = [[0 for y in range(len(Ynum))] for x in range(len(Xnum))]
for x in range(len(Xnum)):
    for y in range(len(Ynum)):
        XY[x][y]=min(X[Xnum[x]],Y[Ynum[y]])

YZ = [[0 for z in range(len(Znum))] for y in range(len(Ynum))]
for y in range(len(Ynum)):
    for z in range(len(Znum)):
        YZ[y][z]=min(Y[Ynum[y]],Z[Znum[z]])
"""
print("\n")
print("XY : ")       
#max-min of XY,YZ
union = [[0 for z in range(len(Znum))] for x in range(len(Xnum))]
for x in range(len(Xnum)):
    print(union[x])
"""

print("\n")
print("Compliment of XY : ")
cxy = [[0 for y in range(len(Ynum))] for x in range(len(Xnum))]
#Compliment of XY
for x in range(len(Xnum)):
    for y in range(len(Ynum)):
        cxy[x][y]=1.0 - XY[x][y]
    print(cxy[x])

print("\n")
print("Compliment of YZ : ")
cyz = [[0 for z in range(len(Znum))] for y in range(len(Ynum))]
#Compliment of XY
for y in range(len(Ynum)):
    for z in range(len(Znum)):
        cyz[y][z]=1.0 - YZ[y][z]
    print(cyz[y])

print("\n")
print("Union of XY and YZ : ")       
#max-min of XY,YZ
union = [[0 for z in range(len(Znum))] for x in range(len(Xnum))]
for x in range(len(Xnum)):
    for z in range(len(Znum)):
        union[x][z]=max(XY[x][z],YZ[x][z])
    print(union[x])

print("\n")
print("Intersection of XY and YZ : ")       
#max-min of XY,YZ
intersection = [[0 for z in range(len(Znum))] for x in range(len(Xnum))]
for x in range(len(Xnum)):
    for z in range(len(Znum)):
        intersection[x][z]=min(XY[x][z],YZ[x][z])
    print(intersection[x])

print("\n")
print("Max-Min of XY and YZ : ")       
#max-min of XY,YZ
maxmin = [[0 for z in range(len(Znum))] for x in range(len(Xnum))]
for x in range(len(Xnum)):
    for z in range(len(Znum)):
        mx=0
        for y in range(len(Ynum)):
            mx=max(mx,min(XY[x][y],YZ[y][z]))
        maxmin[x][z]=mx
    print(maxmin[x])

print("\n")
print("Max-Prod of XY and YZ : ")       
#max-min of XY,YZ
maxprod = [[0 for z in range(len(Znum))] for x in range(len(Xnum))]
for x in range(len(Xnum)):
    for z in range(len(Znum)):
        mx=0
        for y in range(len(Ynum)):
            mx=max(mx,(XY[x][y]*YZ[y][z]))
        maxprod[x][z]=mx
    print(maxprod[x])
