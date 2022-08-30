class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def rev(m):
            m.reverse()
            for i in range(len(m)):
                for j in range(i):
                    m[i][j] ,m[j][i] = m[j][i],m[i][j]
            return m
        count = 0 
        while count != 4:
            if mat == target:
                return True
            else:
                mat = rev(mat)
                count += 1
        else:
            return False
        