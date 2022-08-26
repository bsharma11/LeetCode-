# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        print(root,subRoot)
        self.a = []
        def inorder1(node):
            if node.left == None:
                self.a.append(-1)
            if node.right == None:
                self.a.append(-2)
            if node.left != None:
                inorder1(node.left)
            self.a.append(node.val)
            if node.right != None:
                inorder1(node.right)
            
            
        self.c = []
        def call(node):
            if node == None:return
            inorder1(node)
            self.c.append(self.a)
            self.a = []
            call(node.left)
            call(node.right)
        call(root)
        print(self.c)
        
        self.b = []
        def inorder2(node):
            if node.left == None:
                self.b.append(-1)
            if node.right == None:
                self.b.append(-2)
            if node.left != None:
                inorder2(node.left)
            self.b.append(node.val)
            if node.right != None:
                inorder2(node.right)
        inorder2(subRoot)
        print(self.b)
        if self.b in self.c:return True
        else:return False
