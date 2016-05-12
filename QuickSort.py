# -*- coding: utf-8 -*-
"""
Created on Sat Apr 09 10:52:03 2016

@author: deepsidhpura777
"""

numbers = []
print "Enter size:"
n = int(raw_input())
print "Enter the numbers:"
for i in range(n):
    t = int(raw_input())
    numbers.append(t)
    

    
def QuickSort(a,p,r):
    if (p < r):
        q = Partition(a,p,r)
        QuickSort(a,p,q-1)
        QuickSort(a,q+1,r)

def Partition(a,p,r):    #### i value keeps a track of the latest value less than pivot.
                         #### i+1 will always be a value greater than the pivot, hence exchanged.
    i = p-1
    j = p
    pivot = a[r]
    while j < r:
        if a[j] < pivot:
            i = i + 1   ##### Always exchange the i+1 th value, as it will be greater than pivot.
            c = a[j]
            a[j] = a[i]
            a[i] = c
           
        j = j + 1
    c = a[i+1]
    a[i+1] = pivot
    a[r] = c
     
    return i+1
    
QuickSort(numbers,0,len(numbers)-1)
print numbers

    
        
    