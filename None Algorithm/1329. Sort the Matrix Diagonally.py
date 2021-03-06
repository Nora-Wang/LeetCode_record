Given a m * n matrix mat of integers, sort it diagonally in ascending order from the top-left to the bottom-right then return the sorted array.

 

Example 1:


Input: mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
Output: [[1,1,1,1],[1,2,2,2],[1,2,3,3]]
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 100
1 <= mat[i][j] <= 100


# 斜着取数的规律：j - i的值相等

code:
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        if not len(mat) or not len(mat[0]):
            return []
        
        record = collections.defaultdict(list)
        n, m = len(mat), len(mat[0])
        
        for i in range(n):
            for j in range(m):
                record[i - j].append(mat[i][j])
            
        for k in record:
            record[k].sort(reverse=True)
            
        for i in range(n):
            for j in range(m):
                mat[i][j] = record[i - j].pop()
        
        return mat
        
# 繁琐solution
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        n, m = len(mat), len(mat[0])
        
        # get info
        col_record = [[] for _ in range(n)]
        for row in range(n):
            r, c = row, 0
            while r < n and c < m:
                col_record[row].append(mat[r][c])
                r += 1
                c += 1
        
        row_record = [[] for _ in range(m)]
        for col in range(1, m):
            r, c = 0, col
            while r < n and c < m:
                row_record[col].append(mat[r][c])
                r += 1
                c += 1
        
        # put it back
        for row in range(n):
            r, c = row, 0
            temp = sorted(col_record[row])
            for num in temp:
                mat[r][c] = num
                r += 1
                c += 1
        
        for col in range(m):
            r, c = 0, col
            temp = sorted(row_record[col])
            for num in temp:
                mat[r][c] = num
                r += 1
                c += 1
        
        return mat
        
        
        
