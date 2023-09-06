class Node():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
from collections  import deque
def rightview_recursive(root,level,res):
    if not root:
        return 
    if len(res)==level:
        res.append(root.data)
    rightview_recursive(root.right,level+1,res)
    rightview_recursive(root.left,level+1,res)

def rightview_iterative(root):
    if not root:
        return []
    queue = deque([(root, 0)])
    ans=[]
    while queue:
        node, level = queue.popleft()
        if level==len(ans):
            ans.append(node.data)
        if node.right:
            queue.append((node.right, level+1))
        if node.left:
            queue.append((node.left, level+1))
    print(ans)

root=Node(4)
root.left=Node(5)
root.right=Node(2)
root.right.left=Node(3)
root.right.right=Node(1)
root.right.left.left=Node(6)
root.right.left.right=Node(7)
res=[]
rightview_recursive(root,0,res)
print(res)
rightview_iterative(root)