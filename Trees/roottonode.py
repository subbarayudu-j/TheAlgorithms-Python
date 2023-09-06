class Node():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def root_to_node(root,ans,x):
    if not root:
        return False
    ans.append(root.data)
    if root.data==x:
        return True
    if root_to_node(root.left,ans,x) or root_to_node(root.right,ans,x):
        return True
    ans.pop()
    return False


root=Node(4)
root.left=Node(5)
root.right=Node(2)
root.right.left=Node(3)
root.right.right=Node(1)
root.right.left.left=Node(6)
root.right.left.right=Node(7)

ans=[]
root_to_node(root,ans,6)
print(ans)