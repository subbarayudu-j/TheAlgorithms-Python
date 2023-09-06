class Node():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

from collections import deque
def zigzag(root):
    if not root:
        return []
    queue=deque([root])
    ans=[]
    flag=0
    while queue:
        temp=[]
        for _ in range(len(queue)):
            node=queue.popleft()
            temp.append(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        if flag==0:
            ans.append(temp)
            flag=1
        else:
            ans.append(temp[::-1])
            flag=0
    return ans

root=Node(4)
root.left=Node(5)
root.right=Node(2)
root.right.left=Node(3)
root.right.right=Node(1)
root.right.left.left=Node(6)
root.right.left.right=Node(7)

print(zigzag(root))