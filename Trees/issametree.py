class Node():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def issametree(p,q):
    if not p and not q:
        return True
    if not q or not p:
        return False
    if p.val != q.val:
        return False
    return issametree(p.right, q.right) and issametree(p.left, q.left)

