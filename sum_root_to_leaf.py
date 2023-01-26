
#https://leetcode.com/problems/sum-root-to-leaf-numbers/description/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    current_numbers: list[str] = []

    def rec( self, node: TreeNode, current_str: str) -> None: 

        if not node.left and not node.right: # it is a leaf 
            # if it is a leaf, add to the numbers 
            self.current_numbers.append(f"{current_str}{node.val}")
        else: 
            if node.left: 
                self.rec( node.left, current_str + str(node.val))
            if node.right: 
                self.rec( node.right, current_str + str(node.val))
            

    def sumNumbers(self, root: TreeNode) -> int:
        if not root: return 0 
        self.current_numbers = [] 
        """because leetcode uses one object for all the cases,
         the self.current_nunbers are going to be appended every time the sumNumbers is called, so it has to be cleared
        """
        self.rec( root, "")

        numbers = list(map( int, self.current_numbers ))

        return sum(numbers)
