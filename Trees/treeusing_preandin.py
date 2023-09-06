class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def build_tree_using_inorder_and_preorder(preorder,inorder):
    if not inorder:
        return None
    root = Node(preorder[0])
    mid = inorder.index(preorder[0])
    root.left = build_tree_using_inorder_and_preorder(preorder[1:mid+1],inorder[:mid])
    root.right = build_tree_using_inorder_and_preorder(preorder[mid+1:],inorder[mid+1:])
    return root

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
print(build_tree_using_inorder_and_preorder(preorder,inorder))