class Node():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

from collections import deque
def max_width(root):
    queue=deque([(root,1)])
    ans=0
    while queue:
        n=len(queue)
        ans=max(ans,queue[-1][1]-queue[0][1]+1)
        for _ in range(n):
            node,number=queue.popleft()
            if node.left:
                queue.append((node.left,2*number))
            if node.right:
                queue.append((node.right,2*number +1))
    return ans

root=Node(4)
root.left=Node(5)
root.right=Node(2)
root.right.left=Node(3)
root.right.right=Node(1)
root.right.left.left=Node(6)
root.right.left.right=Node(7)

print(max_width(root))