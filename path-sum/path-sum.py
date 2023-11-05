# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        def recur(node, cur_sum):
            if not node:
                return False
            if not node.right and not node.left and cur_sum + node.val == targetSum:
                return True
            return recur(node.left,cur_sum + node.val) or recur(node.right,cur_sum + node.val)
        return recur(root,0)
                
            
            
        