class Node:
   def __init__(self,data):
       self.left = None
       self.right = None
       self.data = data

def inOrder(root):
   if root:
       inOrder(root.left)
       print (root.data)
       inOrder(root.right)

def preOrder(root):
   if root:
       print (root.data)
       preOrder(root.left)
       preOrder(root.right)

def postOrder(root):
   if root:
       postOrder(root.left)
       postOrder(root.right)
       print (root.data)

#making the tree 
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print inOrder(root)
#4 2 5 1 3
print preOrder(root)
#1 2 4 5 3
print postOrder(root)
#4 5 2 3 1
