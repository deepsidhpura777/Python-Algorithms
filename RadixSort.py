# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 12:27:29 2016

@author: it-lab412
"""

numbers = []
print "Enter Size"
n = int(raw_input())
print "Enter the respective numbers"
for i in range(n):
    t = int(raw_input())
    numbers.append(t)
    
bucket = []
temp = []
for i in range(10):
    bucket.append([])
    
def extract(number,digit):
    if digit == 0:
        return number % 10
    if digit == 1:
        number = number / 10
        return number % 10
    if digit == 2:
        return number / 100
        
for i in range(3):
    for j in range(len(numbers)):
        d = extract(numbers[j],i)
        bucket[d].append(numbers[j])
    for k in range(10):
        temp = temp + bucket[k]
        bucket[k] = []
    numbers = temp
    temp = []
print numbers
    
