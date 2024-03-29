# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        stack = []
        rangeSum = 0
        current = root
        
        while current or stack:
            
            while current:
                
                stack.append(current)
                current = current.left
            popped = stack.pop()
            
            if low<=popped.val<=high:  
                rangeSum += popped.val
            current = popped.right
        return rangeSum
                
        