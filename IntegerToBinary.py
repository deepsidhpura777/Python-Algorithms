# -*- coding: utf-8 -*-
"""
Created on Fri Apr 08 15:13:37 2016

@author: deepsidhpura777
"""

class Stack:
    
    def __init__(self):
        self.items = []
        
    def push(self,x):
        self.items.append(x)
    def pop(self):
        return self.items.pop()
    def isEmpty(self):
        return self.items == []
    
    
print "Enter a Number"
n = int(raw_input())
s = Stack()
temp = n
answer = ''

while temp != 0:
    r = temp % 2
    s.push(r)
    temp = temp / 2
    
while not s.isEmpty():
    answer = answer + str(s.pop())

print answer