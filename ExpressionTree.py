
class Stack:
	def __init__(self):
		self.items = []
	def push(self,value):
		self.items.append(value)
	def pop(self):
		return self.items.pop()
	def isEmpty(self):
		return self.items == []

class Node:
	def __init__(self):
		self.key = ""
		self.left = None
		self.right = None
		
def inorder(node):
	if node == None:
		return
	else:
		inorder(node.left)
		print node.key,
		inorder(node.right)
		
exp = ""
print "Enter Postfix expression:"
exp = raw_input()
s = Stack()

for i in range(len(exp)):
	
	if ord(exp[i]) >= 97 and ord(exp[i]) <= 122:
		node = Node()
		node.key = exp[i]
		s.push(node)
		
	else:
		node = Node()
		node.key = exp[i]
		node.right = s.pop()
		node.left = s.pop()
		s.push(node)

inorder(s.pop())
		
		

		
