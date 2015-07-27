# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def sumTree(node, sum, prefix):
    
    prefix += node.val
    print sum, prefix
    if node.left == None and node.right == None:
        if prefix == sum: return True

    if node.left != None:        
        if sumTree(node.left, sum, prefix): return True

    if node.right != None:
        if sumTree(node.right, sum, prefix): return True

    return False

class Solution:
    # @param {TreeNode} root
    # @param {integer} sum
    # @return {boolean}
    def hasPathSum(self, root, sum):
        if root == None: return False

        return sumTree(root, sum, 0)
        