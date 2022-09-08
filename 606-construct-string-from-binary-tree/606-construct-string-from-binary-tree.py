# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        str1 = ""
        if(root == None):
            return ""
        
        str1 += str(root.val)
        
        if (root.left != None or root.right != None):
            str1 += "(" + self.tree2str(root.left) + ")"
            
        if (root.right != None):
            str1 += "(" + self.tree2str(root.right) + ")"          
        
        return str1              