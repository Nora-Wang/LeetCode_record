Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given binary search tree:  root = [6,2,8,0,4,7,9,null,null,3,5]


 

Example 1:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
Example 2:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
 

Note:

All of the nodes' values will be unique.
p and q are different and both values will exist in the BST.


'''
brute force
record the path from root to p/q, compare them, to find the last same node
time: O(n), space: O(n)


optimize
#####Utilize BST(Version 2)
compare the value of curt root, p, q;
root < p and root < q, go to root.right part
root > p and root > q, go to root.left part
root in the range of p and q, return root



#####Not use BST(236) Version 1
1. input 
root, p, q

2. output
LCA node

3. recursion rule
p/q not exist in curt root, return None
p exist in root.left, q exist in root.right, return curt root
p and q exist in root.left/root.right, return root.left/root.right

4. base case
if root == None/root = q/p, return root

time: O(n), space: O(1)
'''





这道题要与236做对比,这道题明确说了是BST,因此需要用到BST的特性 左节点<根<=右节点 来解题,即version 2;
而236则只是说是binary tree,因此只能用version 1


code:
Version 1
同236题，可直接当作一个binary tree处理
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root == p or root == q or not root:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p ,q)
        
        if left and right:
            return root
        
        if left:
            return left
        
        if right:
            return right
        
        return None
        
        
        
Version 2(更优)
利用BST的特点，左节点<根<=右节点
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root
      
        #当root的值比p,q的值都大时，证明p,q一定在root的左子树上
        if root.val > p.val and root.val > q.val:
            root = self.lowestCommonAncestor(root.left, p, q)
            
        #当root的值比p,q的值都小时，证明p,q一定在root的右子树上
        if root.val < p.val and root.val < q.val:
            root = self.lowestCommonAncestor(root.right, p ,q)
        
        #当p,q分别在左右子树中时，最小公共祖先一定为root
        return root
