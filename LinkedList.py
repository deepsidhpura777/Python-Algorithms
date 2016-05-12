# -*- coding: utf-8 -*-
"""
Created on Thu Apr 07 22:05:39 2016

@author: deepsidhpura777
"""

class LinkNode:
    
    def __init__(self):
        self.value = 0
        self.previous = None
        self.next = None
        
class LinkList:     ####### I am maintaining another list for the nodes, actually it should only be traversed by its head
    
    def __init__(self):
        self.items = []
        
    def add(self,x):
        node = LinkNode()
        node.value = x
        if self.items == []:
            node.previous = None
            node.next = None
        else:
            temp = self.items[len(self.items)-1]
            node.previous = temp
            temp.next = node
            node.next = None
        self.items.append(node)
        
    def delete(self,x):
        
        for i in range(len(self.items)):
            if self.items[i].value == x:
                temp = self.items[i]
                
        if temp.previous == None:
            nex = temp.next
            nex.previous = None
            self.items.remove(temp)
            
            
        elif temp.next == None:
            pre = temp.previous
            pre.next = None
            self.items.remove(temp)
            
        
        else:
            pre = temp.previous
            nex = temp.next
            pre.next = nex
            nex.previous = pre
            self.items.remove(temp)
            
    def split(self):
        link1 = LinkList()
        link2 = LinkList()
        for i in range(len(self.items)/2):
            link1.add(self.items[i].value)
            
        for i in range(len(self.items)/2):
            link2.add(self.items[-i-1].value)
            
        return link1,link2
            
            
    def display(self):

        for i in range(len(self.items)):
            print self.items[i].value
            
    
class LinkedII:

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
            node = LinkNode()
            node.value = x
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = node
            node.previous = temp
            node.next = None
            
    def delete(self,x):
        temp = self.head
        while temp.value != x:
            temp = temp.next
        if temp == self.head:
            nex = temp.next
            temp = None
            self.head = nex
            
        elif temp.next == None:
            pre = temp.previous
            temp = None
            pre.next = None

        else:
            pre = temp.previous
            nex = temp.next
            pre.next = nex
            nex.previous = pre
            temp = None     
            
########## Reverse a linked list ####################
    def reverse(self):  #### Give fucking proper naming conventions !!!!
        temp = self.head
        while temp != None:
             
            nex = temp.next
            pre = temp.previous
            if pre == None:
                temp.next = None
                temp.previous = nex
                #print "Previous Values",temp.previous.value
                temp = nex
                
            else:
                temp.next = pre
                temp.previous = nex
               # print "Previous Values",temp.previous.value
                if nex == None:
                    self.head = temp
                temp = nex
        
                
    
                
    def display(self):
        temp = self.head
        while temp != None:
            print temp.value
            temp = temp.next
            
            
            
            
        
        