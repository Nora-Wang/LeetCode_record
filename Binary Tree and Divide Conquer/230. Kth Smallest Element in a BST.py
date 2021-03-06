Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note: 
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Example 1:

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1
Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
traverse the BST follow inorder rules, 
#use recursion to get the final inorder result, find the kth one
time O(n), space O(n)

#use iterate
time O(k), space O(n)
'''

#iterate
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                k -= 1
                
                if k == 0:
                    return root.val
                
                root = root.right
    

#recursion
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if not root:
            return None
        
        self.count = k
        self.result = root.val
        
        self.traverse(root)
        
        return self.result
    
    def traverse(self, root):
        if not root:
            return
        
        self.traverse(root.left)
        
        self.count -= 1
        if self.count == 0:
            self.result = root.val
            return
        
        self.traverse(root.right)
        

