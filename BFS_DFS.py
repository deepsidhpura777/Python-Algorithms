# -*- coding: utf-8 -*-
"""
Created on Wed May 04 11:40:28 2016

@author: Deep Sidhpura
"""

class Vertex:
    def __init__(self):
        self.key = ''
        self.neighbours = {}
        self.visited = False
        
class Graph:
    def __init__(self):
        self.vertices = {}
        self.size = 0
        
    def addVertex(self,key):
        v = Vertex()
        v.key = key
        self.vertices[v.key] = v
        self.size += 1
        
    def addEdge(self,v1,v2,weight=0):
        if v1 not in self.vertices:
            self.addVertex(v1)
        if v2 not in self.vertices:
            self.addVertex(v2)
        self.vertices[v1].neighbours[v2] = weight
      #  self.vertices[v2].neighbours[v1] = weight
        
def bfs(startNode,g):
    
    queue = []
    ctr = 0
   
    while ctr != g.size:
        final.append(startNode)
        ctr += 1
        startNode.visited = True
        
        for i in startNode.neighbours:
            if g.vertices[i].visited == False:
                queue.append(g.vertices[i])
                g.vertices[i].visited = True
                
        if queue != []:
            startNode = queue.pop(0)
            

def dfs(startNode,g,counter):
    final.append(startNode)
    startNode.visited = True
    counter += 1
    nextNode = None
    
    if counter == g.size:
        return True
        
    for i in startNode.neighbours:
        if g.vertices[i].visited == False:
            nextNode = g.vertices[i]
            if dfs(nextNode,g,counter) == True:   ### Same as backtracking but I just dont have to remove the node incase it fails
                return True
                
    return False



g = Graph()
g.addEdge('a','b')
g.addEdge('b','c')
g.addEdge('a','d')
g.addEdge('b','d')  
g.addEdge('d','e')  
g.addEdge('e','b')  
g.addEdge('e','f') 
g.addEdge('f','c') 
final = []
counter = 0
startNode = g.vertices['a']
dfs(startNode,g,counter)
print "DFS path"
for i in range(len(final)):
    print final[i].key
    
g = Graph()
g.addEdge('0','1')
g.addEdge('0','2')
g.addEdge('2','0')
g.addEdge('1','2')
g.addEdge('2','3')

final = []
counter = 0
startNode = g.vertices['2']
dfs(startNode,g,counter)
print "DFS path"
for i in range(len(final)):
    print final[i].key
   
### Call DFS and BFS independantly
            
            