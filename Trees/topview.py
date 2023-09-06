class Node():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

from collections import defaultdict,deque
def topview_iterative(root):
    a=defaultdict(int)
    queue=deque([(root,0)])
    leftmost,rightmost=0,0
    while queue:
        node,level=queue.popleft()
        if not a[level]:
            a[level]=node.data
        if node.left:
            queue.append((node.left,level-1))
            leftmost=min(leftmost,level-1)
        if node.right:
            queue.append((node.right,level+1))
            rightmost=max(rightmost,level+1)
    print([a[i] for i in range(leftmost,rightmost+1)])

def topview_recursive(root,level,res):
    if not root:
        return
    if not res[level]:
        res[level]=root.data
    topview_recursive(root.left,level-1,res)
    topview_recursive(root.right,level+1,res)

root=Node(4)
root.left=Node(5)
root.right=Node(2)
root.right.left=Node(3)
root.right.right=Node(1)
root.right.left.left=Node(6)
root.right.left.right=Node(7)

topview_iterative(root)

res=defaultdict(int)
topview_recursive(root,0,res)
print([res[i] for i in range(min(res),max(res)+1)])
