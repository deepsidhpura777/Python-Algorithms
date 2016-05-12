# -*- coding: utf-8 -*-
"""
Created on Thu Apr 07 21:35:07 2016

@author: deepsidhpura777
"""

class MyDequeue:
    
    def __init__(self):
        self.items = []
        
    def insertFront(self,x):
        self.items.insert(0,x)
        
    def insertRear(self,x):
        self.items.append(x)
        
    def deleteRear(self):
        return self.items.pop()
        
    def deleteFront(self):
        return self.items.pop(0)
        
    def contents(self):
        return self.items
        
    def isEmpty(self):
        return self.items == []
        
        
myQ = MyDequeue()
myQ.insertFront(5)
myQ.insertFront(4)
myQ.insertRear(6)

print myQ.contents()

print myQ.deleteFront()
print myQ.deleteRear()

print myQ.contents()
        