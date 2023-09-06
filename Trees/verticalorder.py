class Node():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

from collections import defaultdict,deque
def verticalorder(root):
    a=defaultdict(list)
    queue=deque([(root,0)])
    while queue:
        node,level=queue.popleft()
        a[level].append(node.data)
        if node.right:
            queue.append((node.right,level+1))
        if node.left:
            queue.append((node.left,level-1))
    
    print(sum([a[i] for i in range(min(a),max(a)+1)],[]))



root=Node(4)
root.left=Node(5)
root.right=Node(2)
root.right.left=Node(3)
root.right.right=Node(1)
root.right.left.left=Node(6)
root.right.left.right=Node(7)

verticalorder(root)
