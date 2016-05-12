# -*- coding: utf-8 -*-
"""
Created on Fri Apr 08 14:41:49 2016

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
        node = LinkNode()
        node.value = x
        
        if self.head == None:
            node.previous = None
            node.next = None
            self.head = node
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
                
            node.previous = temp
            temp.next = node
            node.next = None
            
    def sort(self):
        
        temp = self.head
        
        while temp.next!=None:
            if temp.value > temp.next.value:
                c = temp.value
                temp.value = temp.next.value
                temp.next.value = c
                temp = self.head
            else:
                temp = temp.next
                
    def display(self):
        temp = self.head
        while temp!=None:
            print temp.value
            temp = temp.next
            
             
        