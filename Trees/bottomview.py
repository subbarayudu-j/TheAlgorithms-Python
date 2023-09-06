class Node():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

from collections import defaultdict,deque
def bottomview_iterative(root):
    if not root:
        return []
    queue = deque([(root, 0)])
    ans=defaultdict(int)
    while queue:
        node, level = queue.popleft()
        ans[level]=node.data
        if node.left:
            queue.append((node.left, level-1))
        if node.right:
            queue.append((node.right, level+1))
    print([ans[i] for i in range(min(ans),max(ans)+1)])

def bottomview_recursive(root,level,res):
    if not root:
        return
    res[level]=root.data
    bottomview_recursive(root.left,level-1,res)
    bottomview_recursive(root.right,level+1,res)

root=Node(4)
root.left=Node(5)
root.right=Node(2)
root.right.left=Node(3)
root.right.right=Node(1)
root.right.left.left=Node(6)
root.right.left.right=Node(7)

bottomview_iterative(root)

res=defaultdict(int)
bottomview_recursive(root,0,res)
print([res[i] for i in range(min(res),max(res)+1)])