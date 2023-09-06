class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isleaf(self,root):
        return not root.left and not root.right
    def addleaves(self,root,ans):
        if self.isleaf(root):
            ans.append(root.val)
            return 
        if root.left:
            self.addleaves(root.left,ans)
        if root.right:
            self.addleaves(root.right,ans)
    def boundary(self, root: Optional[TreeNode]) -> List[int]:
        if not root:return []
        ans=[]
        if not self.isleaf(root):
            ans+=[root.val]
        tmp=root.left
        while tmp:
            if not self.isleaf(tmp):
                ans+=[tmp.val]
            if tmp.left:
                tmp=tmp.left
            else:
                tmp=tmp.right
        self.addleaves(root,ans)
        tmp=root.right
        s=[]
        while tmp:
            if not self.isleaf(tmp):
                s.append(tmp.val)
            if tmp.right:
                tmp=tmp.right
            else:
                tmp=tmp.left
        return ans+s[::-1]