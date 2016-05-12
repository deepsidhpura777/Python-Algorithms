# -*- coding: utf-8 -*-
"""
Created on Thu May 05 17:40:39 2016

@author: Deep Sidhpura
"""
import itertools

program = ['I1','I2','I3']
length = [5,10,3]
cost = []
temp = 0
perm = itertools.permutations([0,1,2])
p = []
for i in perm:
    p.append(list(i))  #### itertools only iterate through permutations,separately store them
    for j in range(len(i)):
        for k in range(j+1):
            temp += length[i[k]]
    cost.append(temp)
    temp = 0
    
index = cost.index(min(cost))
seq = p[index]
for i in range(len(seq)):
    print program[seq[i]]