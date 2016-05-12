# -*- coding: utf-8 -*-
"""
Created on Fri Apr 08 14:09:51 2016

@author: deepsidhpura777
"""

class LinkNode:
    
    def __init__(self):
        self.previous = None
        self.value = 0
        self.next = None
        
class LinkList:
    
    def __init__(self,head=None):
        self.head = head
        
    def add(self,x):
        
        if self.head == None:
            node = LinkNode()
            node.value = x
            node.previous = None
            node.next = None
            self.head = node
            
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            node = LinkNode()
            node.value = x
            node.previous = temp
            temp.next = node
            node.next = None
            
    def pushStack(self,x):
        self.add(x)
        
    def pushQueue(self,x):
        
        if self.head == None:
            self.add(x)
        else:
            node = LinkNode()
            node.value = x
            temp = self.head
            node.next = temp
            temp.previous = node
            node.previous = None
            self.head = node
    
    def popStack(self):
        temp = self.head
        while temp.next != None:
            temp = temp.next
        p = temp.previous
        p.next = None
        temp = None
    
    def popQueue(self):
        temp = self.head
        n = temp.next
        n.previous = None
        self.head = n
        temp = None
        
    def display(self):
        temp = self.head
        while temp!=None:
            print temp.value
            temp = temp.next
            
    
        

    
        
        
    
            
            