# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 13:28:42 2016

@author: it-lab412
"""

class Node:
    def __init__(self):
        self.pol = ""
        self.value = 0
        self.flag = 0
        self.next = None
        
class LinkList:
    def __init__(self):
        self.head= None
        
    def add(self,p,v):
        
        node = Node()
        node.pol = p
        node.value = v
        
        if self.head == None:
            self.head = node
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = node
            
    def display(self):
        temp = self.head
        while temp!=None:
            print temp.value,temp.pol
            temp = temp.next
            
            
            
l1 = LinkList()
#l1.add("x2",5)
#l1.add("x",2)
#l1.add("",1)
l1.add("x4",1)
l1.add("x2",1)
l1.add("",2)

l2 = LinkList()
#l2.add("x3",1)
#l2.add("x",1)
#l2.add("",3)
l2.add("x4",1)
l2.add("x2",1)
l2.add("",2)

l1.display()
l2.display()

ans = LinkList()

temp1 = l1.head
temp2 = l2.head

while temp1 != None:
    while temp2 != None:
        if temp1.pol == temp2.pol:
            v = temp1.value + temp2.value
            temp1.flag = 1
            temp2.flag = 1
            ans.add(temp1.pol,v)
        
        temp2 = temp2.next
        
    temp1 = temp1.next
    temp2 = l2.head

print "Completed Addition part"    
temp1 = l1.head
temp2 = l2.head

while temp1!=None:
    if temp1.flag == 0:
        ans.add(temp1.pol,temp1.value)
    temp1 = temp1.next
    
while temp2!=None:
    if temp2.flag == 0:
        ans.add(temp2.pol,temp2.value)
    temp2 = temp2.next
    
ans.display()