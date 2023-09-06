class Node():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

from collections import defaultdict,deque
def levelorder(root):
    if not root:
        return
    a=defaultdict(list)
    queue=deque([(root,0)])
    while queue:
        node,level=queue.popleft()
        a[level].append(node.data)
        if node.left:
            queue.append((node.left,level+1))
        if node.right:
            queue.append((node.right,level+1))
    print(a.values())


root=Node(4)
root.left=Node(5)
root.right=Node(2)
root.right.left=Node(3)
root.right.right=Node(1)
root.right.left.left=Node(6)
root.right.left.right=Node(7)

levelorder(root)