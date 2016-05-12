# -*- coding: utf-8 -*-
"""
Created on Wed May 04 18:55:53 2016

@author: Nidhi Sidhpura
"""


def minmax(a):
    
    if len(a) == 1:
        return a[0],a[0]
    elif len(a) == 2:
        if a[0] < a[1]:
            return a[0],a[1]
        else:
            return a[1],a[0]
            
    else:
        min1,max1 = minmax(a[:len(a)/2])
        min2,max2 = minmax(a[len(a)/2:])
        
        if min1 < min2:
            minimum = min1
        else:
            minimum = min2
            
        if max1 > max2:
            maximum = max1
        else:
            maximum = max2
        
        return minimum,maximum
        
a = [5,4,1,2,3]
print minmax(a)