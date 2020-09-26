题目：
Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree 

          1
         / \
        2   3
       / \     
      4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.



思路：
理解题意最长是4-2-1-3，所以应该是将求左右两边的高度相加(设叶节点高度为1)，再与之前的值做比较，取最大值

注意理解：
之所以能直接将左右两边的高度相加，是因为其高度相当于边的个数，path的长度 = node的个数 - 1 = 边的个数
如1的高度为3，而2的高度为2，3的高度为，4-2-1-3的长度为3

# n = number of nodes in the tree
# time: O(n), space: O(1) ignore recursion; O(n) include recursion


#Simple Version
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        self.count_diameter(root)
        return self.res
        
    def count_diameter(self, root):
        if not root:
            return 0

        left_count = self.count_diameter(root.left)
        right_count = self.count_diameter(root.right)

        #对于叶节点，没有left和right，return max(left_count, right_count) + 1，结果为1；即叶节点的高度为1
        self.res = max(self.res, left_count + right_count)
        
        return max(left_count, right_count) + 1


code：
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        self.count_diameter(root)
        return self.res
        
    def count_diameter(self, root):
        
        if not root:
            return 0

        left_count = self.count_diameter(root.left)
        right_count = self.count_diameter(root.right)

#简单方法在删除下面两个if之后self.res的求解方法不变，是因为？？？？？？？？？？

        #如果左侧有node，则高度+1
        if root.left:
            left_count += 1

        if root.right:
            right_count += 1
            
#这里要注意在求self.res时，还需要与self.res自己比较大小。因为？？？？？
#(我个人觉得这道题不用跟自己做比较啊，因为这直径不肯定是从根的左边高度+右边高度嘛？难道还有其他比这还大的可能？？)
        self.res = max(self.res, left_count + right_count)
        
        #返回当前node的高度
        return max(left_count, right_count)



        
        
