# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
"""
A = [0.1,(0.2,'x2'),(0.4,'x3'),(0.8,'x4'),(1,'x5'),(1,'x6')]

A = [0.1,0.2,0.4,0.8,1,1]
B = [0.3,0.5,0.2,1,1,0.1]
"""

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


print("\n")

print("A Union B : ", end = " ")
for x in A.keys():
    print(max(A[x],B[x]), end = " ")
print("\n")

print("A Intersection B : " , end = " ")
for x in A.keys():
    print(min(A[x],B[x]), end = " ") 
print("\n")

print("Compliment of A : ", end = " ")
for x in A.keys():
    print(round(1-A[x],2), end = " ")
print("\n")
    
print("Compliment of B : ", end = " ")
for x in B.keys():
    print(round(1-B[x],2), end = " ")
print("\n")


    