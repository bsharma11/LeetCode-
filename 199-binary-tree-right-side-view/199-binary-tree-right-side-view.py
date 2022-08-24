# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
		# Edge cases
        if root is None:
            return res
        
        queue = deque() # initialize a queue for BFS
        queue.append(root)
        
        while queue:
            levelSize = len(queue)
            for i in range(levelSize):
                curNode = queue.popleft() 
                if i == levelSize - 1:
					# if i is the levelSize - 1, that means curNode is the right most node in this level.
                    res.append(curNode.val)
                if curNode.left:
					# maintaining a queue
                    queue.append(curNode.left)
                if curNode.right:
					# maintaining a queue
                    queue.append(curNode.right)
        return res
            
            
                
            
        
            
            
        