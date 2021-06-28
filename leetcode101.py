# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        elif not root.left and not root.right:
            return True
        elif not root.left or not root.right:
            return False
        else:
            def match(l,r):
                if not l and not r:
                    return True
                elif not l or not r:
                    return False
                elif l.val!=r.val:
                    return False
                elif l.val==r.val:
                    return match(l.left,r.right) and match(l.right,r.left)
            return match(root.left,root.right) 
    
