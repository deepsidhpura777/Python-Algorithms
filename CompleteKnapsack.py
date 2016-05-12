# -*- coding: utf-8 -*-
"""
Created on Wed May 04 17:32:59 2016

@author: Deep Sidhpura
"""
weight = [2,3,4,5]
benefit = [3,4,5,6]
capacity = 5

weight.insert(0,0)
benefit.insert(0,0)

B = []
for i in range(len(weight)):
    B.append([0]*(capacity+1))

for i in range(1,len(weight)):   ### from 1 to 4
    for j in range(1,capacity+1): ### from 1 to 5
        b = benefit[i] 
        w = weight[i]
        if w <= j:
            if b + B[i-1][j-w] >= B[i-1][j]:
                B[i][j] = b + B[i-1][j-w]
            else:
                 B[i][j] = B[i-1][j]
        else:
            B[i][j] = B[i-1][j]

i = len(weight) - 1
j = capacity
items = []

while i > 0 and j > 0:
    if B[i][j] != B[i-1][j]:
        items.append(i)
        j = j - weight[i]
        i = i - 1
        
    else:
        i = i - 1
        
print items