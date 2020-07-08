题目：
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1


思路：用count记录island的个数，当一个node的值为1，用bfs遍历其上下左右四个点，若为1，则赋值为0
count = 0
for node = 1 in grid:
    self.bfs(node)
    count += 1
return count

注意点：
bfs的时候需要判断一下这个node是否在矩阵范围内，且node的值为1 def node_valiable(self, grid, x, y)
坐标变换数组：对于grid[i][j]的上下左右node，用set类型的dir与x,y加减得到 dir = ([-1,0],[1,0],[0,-1],[0,1])



#3种方法：BFS，DFS，Union Find
#time: O(n * m), space: O(n * m)



#Version DFS
'''
#DFS Version
use recursion to DFS every node in the grid which is '1', and turn it to '0'. count the number of DFS process
'''
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not len(grid) or not len(grid[0]):
            return 0
        
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '0':
                    continue
                
                res += 1
                self.dfs(grid, i, j)
            
        return res
    
    def dfs(self, grid, x, y):
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
            return
        
        if grid[x][y] == '0':
            return
        
        grid[x][y] = '0'
        
        for direct in [(0,1),(0,-1),(1,0),(-1,0)]:
            self.dfs(grid, x + direct[0], y + direct[1])
            
            



#Version BFS
code:
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        
        count = 0
        len_r = len(grid)
        len_c = len(grid[0])
        for i in range(len_r):
            for j in range(len_c):
                if grid[i][j] == '1':
                    self.bfs(grid, i, j)
                    count += 1
        return count
    
    #判断是否访问过该点：
    #1.可以创建一个visited = set()来记录，没有在visited里的node才能进入队列
    #2.直接将该点的值赋值为0，只有值为1的node才能进入队列
    def bfs(self, grid, x, y):
        dir = ([-1,0],[1,0],[0,-1],[0,1])
        queue = collections.deque([(x, y)])
        grid[x][y] = '0'
        while queue:
            x, y = queue.popleft()
            for [move_x,move_y] in dir:
                next_x = x + move_x
                next_y = y + move_y
                #coding style
                if not self.node_valiable(grid, next_x, next_y):
                    continue
                grid[next_x][next_y] = '0'
                queue.append((next_x, next_y))

    
    def node_valiable(self, grid, x, y):
        #coding style：别一行直接写完，要拆开写
        #return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == '1'
        if not (0 <= x < len(grid) and 0 <= y < len(grid[0])):
            return False
        
        if grid[x][y] == 0:
            return False
            
        return True
            

        
        
#Version Union Find
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not len(grid) or not len(grid[0]):
            return 0
        
        self.father = {}
        self.size = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.father[(i,j)] = (i,j)
                    self.size += 1
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '0':
                    continue
                
                x,y = i, j
                #将上下左右的1合并起来
                for direct in [(0,1),(0,-1),(1,0),(-1,0)]:
                    x_ = x + direct[0]
                    y_ = y + direct[1]
                    
                    if self.check(grid, x_, y_):
                        self.union((x,y),(x_,y_))
        
        return self.size
    
    def union(self, point_a, point_b):
        root_a = self.find(point_a)
        root_b = self.find(point_b)
        
        if root_a != root_b:
            self.father[root_a] = root_b
            self.size -= 1
            
    def find(self, point):
        path = []
        
        while self.father[point] != point:
            path.append(point)
            point = self.father[point]
        
        for p in path:
            self.father[p] = point
        
        return point
    
    def check(self, grid, x, y):
        return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == '1'
