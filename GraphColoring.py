# -*- coding: utf-8 -*-
"""
Created on Thu May 05 19:08:48 2016

@author: Deep Sidhpura
"""

def checkColor(vertex,graph,c):
    l = graph[vertex]
    for i in range(len(l)):
        if l[i]==1 and colorVertex[i] != -1:
            if colorVertex[i] == c:
                return False
    return True
    
def colorPlacement(vertex,graph,colorVertex):
    global ctr
    if ctr == len(graph):
        return True
    
    for c in range(colors):
        if checkColor(vertex,graph,c):
            colorVertex[vertex] = c
            ctr +=1
            if colorPlacement(vertex+1,graph,colorVertex) == True:
                return True
            colorVertex[c] = 0
            ctr -=1
    return False


graph = [[0,0,1,0,1],[0,0,1,1,1],[1,1,0,1,0],[0,1,1,0,1],[1,1,0,1,0]]
colors = 3
colorVertex = [-1] * 5
ctr = 0
colorPlacement(0,graph,colorVertex)
print colorVertex