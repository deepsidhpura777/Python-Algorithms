# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 12:59:26 2016

@author: it-lab412
"""

def pascal(row,col):
    if row == 0 and col == 0:
        return 1
    elif row < 0 or col < 0:
        return 0
    else:
        return pascal(row-1,col) + pascal(row-1,col-1)
        
triangle = []
print "Enter Size"
n = int(raw_input())
for i in range(n):
    triangle.append([0] * (i+1))
    
for i in range(n):
    for j in range(i+1):
        triangle[i][j] = pascal(i,j)
        
for i in range(n):
    print triangle[i]
    
