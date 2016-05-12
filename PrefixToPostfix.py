# -*- coding: utf-8 -*-
"""
Created on Thu Apr 07 21:11:54 2016

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
        
    def top(self):
        return self.items[len(self.items)-1]
        
    def contents(self):
        return self.items
        
        
print "Enter an Expression:"
exp = raw_input()
s = Stack()
temp = ''

for i in range(len(exp)):
    
    token = exp[len(exp)-1-i]
    
    if ord(token) >=97 and ord(token)<=122:
        s.push(token)
    else:
        op1 = s.pop()
        op2 = s.pop()
        temp = op1 + op2 + token
        s.push(temp)
        
        
print "The Postfix Expression is:",s.top()
        
        
        
        
        