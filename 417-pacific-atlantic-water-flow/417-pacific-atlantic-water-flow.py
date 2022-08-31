class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.dist = [[1,0], [0,1], [-1,0],[0,-1]]
        def dfs(i,j,x):
            x.add((i,j))
            for di, dj in self.dist:
                a,b = i+di,j + dj
                if (a in range(n) and b in range(m) and (a,b) not in x and heights[i][j]<= heights[a][b]):
                    dfs(a,b,x)
                
        n = len(heights)
        m = len(heights[0])
        atlantic = set()
        pacific = set()
        
        for i in range(n):
            dfs(i,0,pacific)
            dfs(i,m-1,atlantic)
        for i in range(m):
            dfs(n-1,i,atlantic)
            dfs(0,i,pacific)
        a = []
        for i in atlantic:
            if i in pacific:
                a.append(i)
        return a