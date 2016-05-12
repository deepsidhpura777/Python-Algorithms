# -*- coding: utf-8 -*-
"""
Created on Wed May 04 18:07:30 2016

@author: Deep Sidhpura
"""

jobs = ['a','b','c','d','e']
profit = [100,19,27,25,15]
deadline = [2,1,2,1,3]
size = len(deadline)

sort_order = sorted(range(len(profit)),key = lambda k:profit[k],reverse=True)
profit.sort(reverse=True)

temp_jobs = list(jobs)
temp_deadline = list(deadline)

for i in range(size):
    jobs[i] = temp_jobs[sort_order[i]]
    deadline[i] = temp_deadline[sort_order[i]]
    
sequence = [''] * (max(deadline) + 1)
total = 0

for i in range(size):
    if sequence[deadline[i]] == '':
        sequence[deadline[i]] = jobs[i]
        total += profit[i]
        
    else:
        for j in range(deadline[i],0,-1):
            if sequence[j] == '':
                sequence[j] = jobs[i]
                total += profit[i]
                break
            
print sequence[1:]
print total
    