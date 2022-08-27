class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        q = collections.deque()
        res = -float('inf')

        for j in range(0,len(points)):
            while q and points[j][0] - q[0][1] > k:
                q.popleft()
            
            if q:
                res = max(res, q[0][0] + points[j][1] + points[j][0])
            
            while q and q[-1][0] <= points[j][1] - points[j][0]:
                q.pop()
            
            q.append([points[j][1] - points[j][0], points[j][0]])
        
        return res