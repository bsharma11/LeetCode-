class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        columns = len(board[0])
        path = set()
        def dfs(r,c,i):
            if i == len(word):
                return True
            if r<0 or c<0 or r >= rows or c >= columns or board[r][c] != word[i] or (r,c) in path:
                return False
            path.add((r,c))
            res = (dfs(r+1,c,i+1) or 
                   dfs(r-1,c,i+1) or 
                   dfs(r,c+1,i+1) or 
                   dfs(r,c-1,i+1))
            path.remove((r,c))
            return res
    
                    
        for i in range(rows):
            for j in range(columns):
                if dfs(i,j,0):return True
        return False