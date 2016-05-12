class Node:
	 def __init__(self):
		self.key = 0
		self.left = None
		self.right = None
		self.parent = None
		
class BinaryTree:
	def __init__(self):
		self.root = None
		self.items = {}
		
	def add(self,value,parent = None,direction=''):
		node = Node()
		node.key = value
		if parent == None:
			self.root = node
			self.items[str(value)] = node
		else:
			if direction == 'left':
				parent.left = node
				node.parent = parent
				self.items[str(value)] = node
			else:
				parent.right = node
				node.parent = parent
				self.items[str(value)] = node

				
	def inorder(self,node):
		if node == None:
			return
		else:
			self.inorder(node.left)
			print node.key
			self.inorder(node.right)
			
	def preorder(self,node):
		if node == None:
			return
		else:
			print node.key
			self.preorder(node.left)
			self.preorder(node.right)
			
	
	def postorder(self,node):
		if node == None:
			return
		else:
			self.postorder(node.left)
			self.postorder(node.right)
			print node.key
				
			
b = BinaryTree()
b.add(7)  ###  Value ,Parent Direction
b.add(1,b.items['7'],'left')
b.add(9,b.items['7'],'right')
b.add(0,b.items['1'],'left')
b.add(3,b.items['1'],'right')
b.add(2,b.items['3'],'left')
b.add(5,b.items['3'],'right')
b.add(4,b.items['5'],'left')
b.add(6,b.items['5'],'right')
b.add(8,b.items['9'],'left')
b.add(10,b.items['9'],'right')

r = b.root
print "Inorder:"
b.inorder(r)
print "Preorder:"
b.preorder(r)
print "Postorder:"
b.postorder(r)






			
