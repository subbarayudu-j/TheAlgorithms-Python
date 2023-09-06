class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def buildtree(inorder,postorder):
    if not inorder:
        return None
    root=Node(postorder[-1])
    mid=inorder.index(postorder[-1])
    root.left=buildtree(inorder[:mid],postorder[:mid])
    root.right=buildtree(inorder[mid+1:],postorder[mid:-1])
    return root

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
print(buildtree(inorder,postorder))

