# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {TreeNode}
    def lowestCommonAncestor(self, root, p, q):

        if root == None or p == None or q == None:
            return None
            
                        
        if min(q.val, p.val) > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif max(q.val, p.val) < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root
            
        return None