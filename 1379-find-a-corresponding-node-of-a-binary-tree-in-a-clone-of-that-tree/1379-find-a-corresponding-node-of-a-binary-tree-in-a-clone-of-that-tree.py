# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getTargetCopy(self, original, cloned, target):
        """
        :type original: TreeNode
        :type cloned: TreeNode
        :type target: TreeNode
        :rtype: TreeNode
        """
        
        self.target = target.val
        self.ans = None
        def traverse(node):
            if not node:
                return 
            if node.val == self.target:
                self.ans = node
                return 
            traverse(node.left)
            traverse(node.right)
        traverse(cloned)
            
        return self.ans
    
        
            
                
       
                
            
        