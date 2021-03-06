Given a knight in a chessboard (a binary matrix with 0 as empty and 1 as barrier) with a source position, find the shortest path to a destination position, return the length of the route.
Return -1 if destination cannot be reached.

Example
Example 1:

Input:
[[0,0,0],
 [0,0,0],
 [0,0,0]]
source = [2, 0] destination = [2, 2] 
Output: 2
Explanation:
[2,0]->[0,1]->[2,2]
Example 2:

Input:
[[0,1,0],
 [0,0,1],
 [0,0,0]]
source = [2, 0] destination = [2, 2] 
Output:-1
Clarification
If the knight is at (x, y), he can get to the following positions in one step:

(x + 1, y + 2)
(x + 1, y - 2)
(x - 1, y + 2)
(x - 1, y - 2)
(x + 2, y + 1)
(x + 2, y - 1)
(x - 2, y + 1)
(x - 2, y - 1)
Notice
source and destination must be empty.
Knight can not enter the barrier.
Path length refers to the number of steps the knight takes.


易错点:
1.用了grid[new_x][new_y] = 1就不用设置self.visited了
2.有count/step/level就一定要有for _ in range(len_level)
#注意将这里的count与word ladder区分一下,这里的count初始值为0,因为这里需要的是path length;而word ladder需要的是word的个数
3.注意这道题的source和destination是Point类型,使用的时候需要source.x,source.y
4.return的情况要紧跟pop后面


思路：
总体跟numbers of island差不多
要注意一点，每遍历一个node，要将其赋值为1，否则会出现Memory limit exceeded的情况


###########follow up#########
speed up看课后补充，word ladder也可以用相同的方法解决（给出了起点和终点）



code:
"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""

class Solution:
    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path 
    """
        
    def shortestPath(self, grid, source, destination):
        if not grid or not grid[0]:
            return -1
        if source.x == destination.x and source.y == destination.y:
            return 0
            
        move = [[1,2],[1,-2],[-1,2],[-1,-2],[2,1], [2,-1],[-2,1],[-2,-1]]
        
        queue = collections.deque([source])
        count = 0
        #该点已被放入queue，即被遍历，因此需要将其赋值为1，避免重复遍历
        grid[source.x][source.y] = 1
        
        while queue:
            #count记录的是遍历了多少层，因此是在每个level处才+1     
            count += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                #return情况
                if node.x == destination.x and node.y == destination.y:
                    return count
                for move_x, move_y in move:
                #这里一定要用一个new来记录，因为后续node.x和node.y还要用，不能改变其值
                    new_x = node.x + move_x
                    new_y = node.y + move_y
                    #判断其值是否符合条件：在grid范围内+不是false
                    if self.is_valid(grid, new_x, new_y):
                        queue.append(Point(new_x,new_y))
                    #该点已被放入queue，即被遍历，因此需要将其赋值为1，避免重复遍历
                        grid[new_x][new_y] = 1
            
        return -1
    
    #coding style
    def is_valid(self, grid, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
            return False
        
        if grid[i][j] == 1:
            return False
        
        return True
