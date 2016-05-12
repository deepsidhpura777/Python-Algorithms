# -*- coding: utf-8 -*-
"""
Created on Wed May 04 23:27:20 2016

@author: Deep Sidhpura
"""

def subsetSum(a,curSum,desSum,answer,index):
    if curSum > desSum:
        return False
    if curSum == desSum:
        return True
    for i in range(index,len(a)):
        curSum += a[i]
        answer.append(a[i])
        if subsetSum(a,curSum,desSum,answer,i+1) == True:
            return True
        curSum-= a[i]
        answer.remove(a[i])
    return False
    
a = [1,2,3,4,5,6,7]
answer = []
curSum = 0
desSum = 9

print "Part 1"
for i in range(len(a)):
    subsetSum(a,curSum,desSum,answer,i)
    if answer != [] :    
        print answer
    answer = []
    
a = [12,1,3,8,20,50]
answer = []
curSum = 0
desSum = 44

print "Part 2"
for i in range(len(a)):
    subsetSum(a,curSum,desSum,answer,i)
    if answer != [] :    
        print answer
    answer = []