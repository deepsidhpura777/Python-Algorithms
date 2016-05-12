# -*- coding: utf-8 -*-
"""
Created on Wed May 04 10:53:32 2016

@author: Deep Sidhpura
"""

class Node:
    def __init__(self,key,frequency,left=None,right=None,code=''):
        self.key = key
        self.frequency = frequency
        self.left = left
        self.right = right
        self.code = code


def HuffmanCode(node,c=''):
    if node.left == None and node.right == None:
        code[node.key] = c
    else:
        HuffmanCode(node.left,c+'0')
        HuffmanCode(node.right,c+'1')
    
       
nodes = []
code = {}
n1 = Node('a',5)
nodes.append(n1)
n2 = Node('b',9)
nodes.append(n2)
n3 = Node('c',12)
nodes.append(n3)
n4 = Node('d',13)
nodes.append(n4)
n5 = Node('e',16)
nodes.append(n5)
n6 = Node('f',45)
nodes.append(n6)

nodes = sorted(nodes,key = lambda x:x.frequency)

while len(nodes) != 1:
    n1 = nodes.pop(0)
    n2 = nodes.pop(0)
    n = Node('',n1.frequency + n2.frequency,n1,n2)
    nodes.append(n)
    nodes = sorted(nodes,key = lambda x:x.frequency)

HuffmanCode(nodes[0])
print code
