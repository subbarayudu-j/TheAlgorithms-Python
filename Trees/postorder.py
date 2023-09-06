class Node():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def postorder_recursive(root):
    if root:
        postorder_recursive(root.left)
        postorder_recursive(root.right)
        print(root.data)

def postorder_iterative(root):
    st=[]
    while True:
        if root:
            st.append(root)
            root=root.left
        elif st:
            tmp=st[-1].right
            if tmp:
                root=tmp
            else:
                tmp=st.pop()
                print(tmp.data)
                while st and tmp==st[-1].right:
                    tmp=st.pop()
                    print(tmp.data)
        else:
            break

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

postorder_recursive(root)
postorder_iterative(root)