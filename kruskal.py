# -*- coding: utf-8 -*-
"""
Created on Wed May 04 14:07:56 2016

@author: Deep Sidhpura
"""

class Edge:
    def __init__(self,v1,v2,weight):
        self.v1 = v1
        self.v2 = v2
        self.weight = weight
        
class Graph:
    def __init__(self):
        self.edgeList = []
        
    def addEdge(self,v1,v2,weight):
        e = Edge(v1,v2,weight)
        self.edgeList.append(e)
        
def checkCycle(myset,edge):
    if myset[edge.v1] == myset[edge.v2]:
        return True
    else:
        return False
        
g = Graph()
g.addEdge(0,1,4)
g.addEdge(0,7,8)
g.addEdge(1,7,11)
g.addEdge(1,2,8)
g.addEdge(7,8,7)
g.addEdge(7,6,1)
g.addEdge(2,8,2)
g.addEdge(2,5,4)
g.addEdge(8,6,6)
g.addEdge(6,5,2)
g.addEdge(2,3,7)
g.addEdge(3,5,14)
g.addEdge(3,4,9)
g.addEdge(5,4,10)
numVertices = 9
myset = []
for i in range(9):
    s = set()
    s.add(i)
    myset.append(s)
    
g.edgeList = sorted(g.edgeList,key = lambda x:x.weight)
temp = g.edgeList
answer = []
#### minimum spanning tree will have v-1 edges
while len(answer) != numVertices-1:
    e = temp.pop(0)
    if not checkCycle(myset,e):
        union = myset[e.v1] | myset[e.v2]
        for i in list(union):
            myset[i] = union
        answer.append(e)
        
for i in range(len(answer)):
    print answer[i].v1,answer[i].v2,answer[i].weight
        