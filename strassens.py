# -*- coding: utf-8 -*-
"""
Created on Sat May 07 22:11:28 2016

@author: Deep Sidhpura
"""

a = [[1,1,1,1],[2,2,2,2],[3,3,3,3],[4,4,4,4]]
b = [[5,5,5,5],[6,6,6,6],[7,7,7,7],[8,8,8,8]]

def split(matrix):
    a = matrix
    b = matrix
    c = matrix
    d = matrix
    
    a = a[:len(a)/2]  ## a = [[1,1,1,1],[2,2,2,2]]
    b = b[:len(b)/2]
    c = c[len(c)/2:] 
    d = d[len(d)/2:]
    
    for i in range(len(a)):
        a[i] = a[i][:len(a)]
        b[i] = b[i][len(b):]
        c[i] = c[i][:len(c)]
        d[i] = d[i][len(d):]
        
    return a,b,c,d
        
def add(a,b):              ###### Use small examples of 2D list on paper to solve
    if type(a) == int:
        d = a+b
    else:
        d = []
        for i in range(len(a)):
            c = []
            for j in range(len(a)):
                t = a[i][j] + b[i][j]
                c.append(t)
                
            d.append(c)
             
    return d

def sub(a,b):
    if type(a) == int:
        d = a-b
    else:
        d = []
        for i in range(len(a)):
            c = []
            for j in range(len(a)):
                t = a[i][j] - b[i][j]
                c.append(t)
                
            d.append(c)
             
    return d   
    
def strassen(a,b,n):
    if n==1:
        d = [[0]]
        d[0][0] = a[0][0] * b[0][0]   #### Even single values will be a 2 D list
        return d
    else:
        a11,a12,a21,a22 = split(a)
        b11,b12,b21,b22 = split(b)
        
        p1 = strassen(add(a11,a22),add(b11,b22),n/2)
        p2 = strassen(add(a21,a22),b11,n/2)
        p3 = strassen(a11,sub(b12,b22),n/2)
        p4 = strassen(a22,sub(b21,b11),n/2)
        p5 = strassen(add(a11,a12),b22,n/2)
        p6 = strassen(sub(a21,a11),add(b11,b12),n/2)
        p7 = strassen(sub(a12,a22),add(b21,b22),n/2)
        
        c11 = add(sub(add(p1,p4),p5),p7)
        c12 = add(p3,p5)
        c21 = add(p2,p4)
        c22 = add(sub(add(p1,p3),p2),p6)
        
        c = []
        for i in range(len(c11) * 2):
            c.append([0] * (len(c11)*2))
            
        for i in range(len(c11)):
             for j in range(len(c11)):
                 
                 c[i][j] =            c11[i][j]
                 c[i][j + len(c11)] = c12[i][j]
                 c[i + len(c11)][j] = c21[i][j]
                 c[i + len(c11)][j + len(c11)] = c22[i][j]

        return c     
        
print strassen(a,b,4)