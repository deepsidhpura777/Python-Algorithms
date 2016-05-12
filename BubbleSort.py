# -*- coding: utf-8 -*-
"""
Created on Fri Apr 08 15:34:13 2016

@author: deepsidhpura777
"""

numbers = []
ctr = 0

print "Enter Size"
n = int(raw_input())
print "Enter the respective numbers"
for i in range(n):
    temp = int(raw_input())
    numbers.append(temp)
print "Unsorted Numbers",numbers    
while ctr != len(numbers)-1:
    if numbers[ctr] > numbers[ctr+1]:
        c = numbers[ctr]
        numbers[ctr] = numbers[ctr+1]
        numbers[ctr+1] = c
        ctr = 0
    else:
        ctr = ctr + 1
        
print "Sorted Numbers",numbers
