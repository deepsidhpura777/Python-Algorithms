# -*- coding: utf-8 -*-
"""
Created on Thu May 05 16:37:54 2016

@author: Deep Sidhpura
"""

x = 'AGGTAB'
y = 'GXTXAYB'
m = len(x)
n = len(y)
L = [[0]*(n+1) for i in range(m+1)]

########### Finding the length of the common sequence ##################

for i in range(m+1):
    for j in range(n+1):
        if i==0 or j==0:
            L[i][j] = 0
        elif x[i-1] == y[j-1]:
            L[i][j] = L[i-1][j-1] + 1
        else:
            L[i][j] = max(L[i-1][j],L[i][j-1])

########### Finding the common sequence ####################

index = L[m][n]
lcs = [""] * (index+1)
lcs[index] = "\0"
 
i = m
j = n

while i > 0 and j > 0:
 
        # If current character in X[] and Y are same, then
        # current character is part of LCS
            if x[i-1] == y[j-1]:
                lcs[index-1] = x[i-1]
                i-=1
                j-=1
                index-=1
 
        # If not same, then find the larger of two and
        # go in the direction of larger value
            elif L[i-1][j] > L[i][j-1]:
                i-=1
            else:
                j-=1
 
print "lcs of " + x + " and " + y + " is " + "".join(lcs) 

