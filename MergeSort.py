# -*- coding: utf-8 -*-
"""
Created on Fri Apr 08 16:18:48 2016

@author: deepsidhpura777
"""

numbers = []
print "Enter Size"
n = int(raw_input())
print "Enter the Numbers"
for i in range(n):
    t = int(raw_input())
    numbers.append(t)

def MergeSort(a):
    
    if len(a) == 1:
        return a
        
    else:
        p = MergeSort(a[:len(a)/2])
        q = MergeSort(a[len(a)/2:])
        r = Merge(p,q)
        return r
        
def Merge(p,q):
        temp = []
        sentinel = 1000
        values = len(p) + len(q)
        p.append(sentinel)
        q.append(sentinel)
        
        i = 0
        j = 0
        
        while len(temp) != values:
                
            if p[i] < q[j]:
                temp.append(p[i])
                i = i + 1
            if p[i] > q[j]:
                temp.append(q[j])
                j = j + 1
                
        return temp

answer = MergeSort(numbers)
print answer            