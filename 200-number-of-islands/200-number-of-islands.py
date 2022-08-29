class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        
        row = len(grid)
        col = len(grid[0])
        count = 0
        
        
        def bfs(i, j):
            q = collections.deque()
            q.append((i,j))
            while q:
                r,c = q.popleft()
                direction = [[1,0], [-1, 0], [0, 1], [0, -1]]
                for a, b in direction:
                    x,y = a+r,b+c
                    if (x in range(row) and y in range(col) and grid[x][y] == "1" and (x,y) not in visited):
                        visited.add((x,y))
                        q.append((x,y))
   
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1" and (i,j) not in visited:
                    visited.add((i,j))
                    bfs(i,j)
                    count += 1
        return count
                    