# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, a, b) -> bool:
        if a == None and b == None:
            return True
        if a == None or b == None:
            return False
        if a.val != b.val:
            return False
        return (self.isSameTree(a.left,b.left) and self.isSameTree(a.right,b.right))
        
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root:
            if self.isSameTree(root, subRoot):
                return True
            else:
                return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        else:
            return False