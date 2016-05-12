# -*- coding: utf-8 -*-
"""
Created on Wed May 04 14:54:25 2016

@author: Deep Sidhpura
"""

class Vertex:
    def __init__(self):
        self.key = ''
        self.neighbours = {}

class Graph:
    def __init__(self):
        self.vertices = {}
        self.size = 0
        
    def addVertex(self,key):
        v = Vertex()
        v.key = key
        self.vertices[key] = v
        self.size += 1
        
    def addEdge(self,v1,v2,weight):
        if v1 not in self.vertices:
            self.addVertex(v1)
        if v2 not in self.vertices:
            self.addVertex(v2)
        self.vertices[v1].neighbours[v2] = weight
        self.vertices[v2].neighbours[v1] = weight

def findMinimum(mset,distanceValues):
    m = 100
    index = -1
    for i in range(len(distanceValues)):
        if i not in mset:
            if distanceValues[i] < m:
                m = distanceValues[i]
                index = i
                
    return index
        
g = Graph()
g.addEdge('0','1',2)
g.addEdge('0','2',3)
g.addEdge('1','2',1)
g.addEdge('1','3',1)
g.addEdge('1','4',4)
g.addEdge('3','4',1)
g.addEdge('2','5',5)
g.addEdge('4','5',1)
g.addEdge('5','6',1)

mset = []
distanceValues = [0,100,100,100,100,100,100]
parent = {}

while len(mset) != g.size:
    u = findMinimum(mset,distanceValues)
    mset.append(u)
    node = g.vertices[str(u)]
    neigh = node.neighbours
    for i in neigh:
        if int(i) not in mset:
            if distanceValues[u] + neigh[i] < distanceValues[int(i)]:
                distanceValues[int(i)] = distanceValues[u] + neigh[i]
                parent[i] = str(u)
                
for i in parent:
    print parent[i],i,g.vertices[parent[i]].neighbours[i]