# -*- coding: utf-8 -*-
"""
Created on Wed May 04 15:57:33 2016

@author: Deep Sidhpura
"""

items = ['a','b','c','d','e']
weight = [4,8,2,6,1]
benefit = [12,32,40,30,50]
bw = []
capacity = 10
cost = 0
ctr = 0

temp_weight = list(weight)   #### Make sure you make a copy of a list, POINTERS !!!!
temp_benefit = list(benefit)
temp_items = list(items)

for i in range(len(weight)):
    bw.append(benefit[i]/weight[i])
 
   
sort_order = sorted(range(len(bw)),key = lambda x:bw[x],reverse = True)
bw.sort(reverse=True)
for i in range(len(sort_order)):
    
    weight[i] = temp_weight[sort_order[i]]
    benefit[i] = temp_benefit[sort_order[i]]
    items[i] = temp_items[sort_order[i]]

while capacity != 0:
    if capacity - weight[ctr] >= 0:
        capacity -= weight[ctr]
        cost += benefit[ctr]
        print "Item",items[ctr]," Weight",weight[ctr]," Benefit",benefit[ctr]
         
    else:
        cost += capacity * bw[ctr]
        print "Item",items[ctr]," Weight",capacity," Benefit",capacity * bw[ctr] 
        capacity = 0
    ctr += 1
    
print "Total Cost",cost