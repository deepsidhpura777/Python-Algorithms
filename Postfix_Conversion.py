# -*- coding: utf-8 -*-
"""
Created on Wed Apr 06 23:18:23 2016

@author: deepsidhpura777
"""

#==============================================================================
# ############ Converting an expression to Postfix ######################
# 
# #  Create an empty stack called opstack for keeping operators. Create an empty list for output.
# #  Convert the input infix string to a list by using the string method split.
# #  Scan the token list from left to right.
# #  If the token is an operand, append it to the end of the output list.
# #  If the token is a left parenthesis, push it on the opstack.
# #  If the token is a right parenthesis, pop the opstack until the corresponding left parenthesis is removed. Append each operator to the end of the output list.
# #  If the token is an operator, *, /, +, or -, push it on the opstack. However, first remove any operators already on the opstack that have higher or equal precedence and append them to the output list.
# #  When the input expression has been completely processed, check the opstack. Any operators still on the stack can be removed and appended to the end of the output list.
#==============================================================================

class Stack:
    
    def __init__(self):
        self.items = []
        
    def push(self,x):
        self.items.append(x)
        
    def pop(self):
        return self.items.pop()
        
    def top(self):
        return self.items[len(self.items) - 1]
        
    def isEmpty(self):
        return self.items == []
        
    def contents(self):
        return self.items
        
        
print "Enter an expression"
exp = raw_input()
answer = ''
operator_stack = Stack()
bodmas = {'+':2,'-':2,'*':3,'/':3,'(':1}

for i in range(len(exp)):
    
        
        if ord(exp[i]) >= 97 and ord(exp[i]) <= 122:
            answer = answer + exp[i]
            
        elif exp[i] == '(':
            operator_stack.push('(')
            
        elif exp[i] == ')':
            top = operator_stack.pop()
            while top != '(':
                answer = answer + top
                top = operator_stack.pop()
                
        else:
            while not operator_stack.isEmpty() and bodmas[operator_stack.top()] > bodmas[exp[i]]:
                answer = answer + operator_stack.pop()
            operator_stack.push(exp[i])
            
while not operator_stack.isEmpty():
    answer = answer + operator_stack.pop()

print "The Postfix Expression is:",answer            
        
                        
            
    



