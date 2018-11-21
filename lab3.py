# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 11:01:07 2018

@author: BIT
"""
import numpy as np

s= input()
Amem = list(map(str, s.split()))
s= input()
Aval = list(map(float, s.split()))
A = {}
for x in range(len(Amem)):
    A[Amem[x]]=Aval[x]

s= input()
Bmem = list(map(str, s.split()))
s= input()
Bval = list(map(float, s.split()))
B = {}
for x in range(len(Bmem)):
    B[Bmem[x]]=Bval[x]
    if Bmem[x] not in A:
        A[Bmem[x]]=0

for x in range(len(Amem)):
    if Amem[x] not in B:
        B[Amem[x]]=0

print("\n")

euclid = 0.0
print("Euclidien Distance : ", end = " ")
for x in A.keys():
    euclid = euclid + np.power(A[x]-B[x],2)
euclid = np.sqrt(euclid)
print(euclid)
print("\n")

ham = 0.0
print("Hamming Distance : ", end = " ")
for x in A.keys():
    ham = ham + np.abs(A[x]-B[x])
print(ham)
print("\n")