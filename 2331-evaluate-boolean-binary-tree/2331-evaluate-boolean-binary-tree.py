# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def evaluateTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root.left:
            return bool(root.val)
        boolean = root.val
        if boolean == 2:
            return bool(self.evaluateTree(root.left) or self.evaluateTree(root.right))
        else:
            return bool(self.evaluateTree(root.left) and self.evaluateTree(root.right))
        
        
                
        