class Node():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def inorder_recursive(root):
    if root:
        inorder_recursive(root.left)
        print(root.data)
        inorder_recursive(root.right)

def inorder_iterative(root):
    stack = []
    current = root
    while True:
        if current:
            stack.append(current)
            current = current.left
        elif stack:
            current = stack.pop()
            print(current.data)
            current = current.right
        else:
            break

def moris_inorder(root):
    current = root
    while current:
        if current.left:
            pre = current.left
            while pre.right and pre.right != current:
                pre = pre.right
            if pre.right == current:
                pre.right = None
                print(current.data)
                current = current.right
            else:
                pre.right = current
                current = current.left
        else:
            print(current.data)
            current = current.right
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
inorder_recursive(root)
inorder_iterative(root)
