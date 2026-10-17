# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def height(self, root):
       
        if root is None:
            return 0
        return 1 + max(self.height(root.left), self.height(root.right))

    def isBalanced(self, root):
        if root is None:
            return True
        lefHeight = self.height(root.left)
        rightHeight = self.height(root.right)

        if abs(lefHeight - rightHeight) > 1:
            return False
        
        return self.isBalanced(root.left) and self.isBalanced(root.right)
        