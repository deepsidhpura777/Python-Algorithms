# -*- coding: utf-8 -*-
"""
Created on Wed Apr 06 22:14:22 2016

@author: deepsidhpura777
"""

######## Postfix Evaluation ###############

class Stack:
    
    def __init__(self):
        self.items = []
        
    def push(self,x):
        self.items.append(x)
        
    def pop(self):
        return self.items.pop()
        
    def isEmpty(self):
        if self.items == []:
            return True   
        else:
            return False
            
    def contents(self):
        return self.items
            
            
print "Enter the expression:"
expression = raw_input()   #### abc*+  , ab*c+
v = {}   ### Dictionary to take string values
value = Stack()
myStack = Stack()
answer = 0

for i in range(len(expression)):
    if ord(expression[i]) >= 97 and ord(expression[i]) <=122:
        print "Enter the value of",expression[i]
        temp = int(raw_input())
        v[expression[i]] = temp
        
        
for i in range(len(expression)):
    if ord(expression[i]) >= 97 and ord(expression[i]) <=122:
        myStack.push(expression[i])
        value.push(v[expression[i]])
        
        
    else:
        v1 = value.pop()
        v2 = value.pop()
        if expression[i] == '+':
            answer = v1 + v2
        
        if expression[i] == '-':
            answer = v1 - v2
            
        if expression[i] == '*':
            answer = v1 * v2
            
        if expression[i] == '/':
            answer = v2 / v1
            
        value.push(answer)
        
print "The answer is:",value.contents()


    
    
    

    
    

