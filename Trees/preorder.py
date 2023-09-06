class Node():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def preorer_recursive(root):
    if root:
        print(root.data)
        preorer_recursive(root.left)
        preorer_recursive(root.right)

def preorder_iterative(root):
    st=[]
    while 1:
        if root:
            print(root.data)
            st.append(root)
            root=root.left
        elif st:
            tmp=st.pop()
            root=tmp.right
        else:
            break

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

preorer_recursive(root)

preorder_iterative(root)