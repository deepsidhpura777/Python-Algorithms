# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 12:07:34 2016

@author: it-lab412
"""

def gapInsertionSort(start,a,gap):
    
    #print "Start",start
    
    for i in range(start+gap,len(a),gap):
        temp = i
        key = a[temp]
        while key < a[temp-gap] and temp!=start:
            a[temp] = a[temp-gap]
            temp = temp - gap
        a[temp] = key


numbers = []
print "Enter Size"
n = int(raw_input())
print "Enter the respective numbers"
for i in range(n):
    t = int(raw_input())
    numbers.append(t)
    

    
gap = len(numbers) / 2
while gap > 0:
    for i in range(gap):
        gapInsertionSort(i,numbers,gap)
    gap = gap / 2
    

print numbers       