# -*- coding: utf-8 -*-
"""
Created on Fri Apr 08 15:44:34 2016

@author: deepsidhpura777
"""

numbers = []
key = 1

print "Enter Size"
n = int(raw_input())

print "Enter the respective numbers"
for i in range(n):
    t = int(raw_input())
    numbers.append(t)
    
print "Unsorted Numbers",numbers
    
while key < len(numbers):
    
    temp = key
    v = numbers[key]
#    while (numbers[temp] < numbers[temp-1] and temp != 0):
#        t = numbers[temp]
#        numbers[temp] = numbers[temp-1]
#        numbers[temp-1] = t
#        temp = temp - 1
     
    while (v < numbers[temp-1] and temp != 0):
        numbers[temp] = numbers[temp-1]
        temp = temp - 1
    numbers[temp] = v
    key = key + 1
    
print "Sorted Numbers",numbers
        