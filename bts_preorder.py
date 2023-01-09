# https://leetcode.com/problems/binary-tree-preorder-traversal/description/

#Definition for a binary tree node.
 class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


def preorderTraversal( root: TreeNode) -> list[int]:
        res = []
        def recur(root) -> None:
            nonlocal res
            if not root: return 
            res.append( root.val )

            recur( root.left)
            recur( root.right) 

        recur(root)
        return res
