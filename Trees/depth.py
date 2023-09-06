class Node():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

from collections import deque
def depth(root):
    if not root:
        return 0
    return 1+max(depth(root.left),depth(root.right))

def depth_iterative(root):
    if not root:
        return 0
    queue=deque([(root,1)])
    ans=0
    while queue:
        node,level=queue.popleft()
        ans=max(ans,level)
        if node.left:
            queue.append((node.left,level+1))
        if node.right:
            queue.append((node.right,level+1))
    return ans

root=Node(4)
root.left=Node(5)
root.right=Node(2)
root.right.left=Node(3)
root.right.right=Node(1)
root.right.left.left=Node(6)
root.right.left.right=Node(7)

print(depth(root))
print(depth_iterative(root))