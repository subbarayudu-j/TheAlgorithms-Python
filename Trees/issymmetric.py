class Node():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def issymmetric(root):
    if not root:    
        return True
    def helper(left,right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.data!=right.data:
            return False
        return helper(left.left,right.right) and helper(left.right,right.left)
    return helper(root.left,root.right)

root=Node(4)
root.left=Node(5)
root.right=Node(2)
root.right.left=Node(3)
root.right.right=Node(1)
root.right.left.left=Node(6)
root.right.left.right=Node(7)
print(issymmetric(root))

# Path: trees\levelorder.py?