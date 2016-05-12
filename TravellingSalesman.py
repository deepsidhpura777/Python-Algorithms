# -*- coding: utf-8 -*-
"""
Created on Thu May 05 17:58:00 2016

@author: Deep Sidhpura
"""
import itertools

class Vertex:
    def __init__(self):
        self.key = ''
        self.neighbours = {}

class Graph:
    def __init__(self):
        self.vertices = {}
        self.size = 0
        
    def addVertex(self,k):
        v = Vertex()
        v.key = k
        self.vertices[k] = v
        self.size += 1
    
    def addEdge(self,v1,v2,w):
        if v1 not in self.vertices:
            self.addVertex(v1)
        if v2 not in self.vertices:
            self.addVertex(v2)
        
        self.vertices[v1].neighbours[v2] = w
        self.vertices[v2].neighbours[v1] = w
        
g = Graph()
g.addEdge('1','2',2)
g.addEdge('1','3',3)
g.addEdge('1','4',4)
g.addEdge('1','5',5)
g.addEdge('2','3',8)
g.addEdge('2','4',9)
g.addEdge('2','5',10)
g.addEdge('3','4',14)
g.addEdge('3','5',15)
g.addEdge('4','5',20)

startNode = g.vertices['1']
neighboursList = startNode.neighbours.keys()
n = len(neighboursList)
perm = itertools.permutations(neighboursList)
distance = []
temp = 0
p = []

for i in perm:
    p.append(list(i))
    temp += startNode.neighbours[i[0]]
    for j in range(n-1):
        temp += g.vertices[i[j]].neighbours[i[j+1]]
    temp += startNode.neighbours[i[j+1]]
    distance.append(temp)
    temp = 0
    
index = distance.index(min(distance))
seq = p[index]
seq.insert(0,'1')
seq.append('1')
print seq
print min(distance)