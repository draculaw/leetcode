# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def myinvert(root):
    if root == None:
        return
    left = root.left
    root.left = root.right
    root.right = left
    myinvert(root.left)
    myinvert(root.right)
    
class Solution:
    # @param {TreeNode} root
    # @return {TreeNode}
    def invertTree(self, root):
        if root == None:
            return None
        if root.left == None and root.right == None:
            return root
            
        myinvert(root)
        
        return root
        