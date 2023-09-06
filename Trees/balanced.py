class Node():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

from collections import deque
def isbalanced(root):
    if root is None:
        return 0
    lh = isbalanced(root.left)
    if lh == 0:
        return 0
    rh = isbalanced(root.right)
    if rh == 0:
        return 0
    if (abs(lh - rh) > 1):
        return 0
    else:
        return max(lh, rh) + 1

# def is_balanced_iterative(root):
    
root=Node(4)
root.left=Node(5)
root.right=Node(2)
root.right.left=Node(3)
root.right.right=Node(1)
root.right.left.left=Node(6)
root.right.left.right=Node(7)

if isbalanced(root)==0:
    print('not balanced')
else:
    print('balanced')
# print(is_balanced_iterative(root))