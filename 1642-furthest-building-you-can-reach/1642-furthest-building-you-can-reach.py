class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n= len(heights)
        
        q= []
        
        heapq.heapify(q)
        total_bricks_remaining =bricks
        
        for j in range(n-1):
            diff = heights[j+1]- heights[j]
            if diff <=0: continue
            
            if len(q)==ladders:
                #use somebricks
                heapq.heappush(q, diff)
                
                smallest_cost = heapq.heappop(q)
                total_bricks_remaining -= smallest_cost
                
                if total_bricks_remaining<0 : return max(j, 0)
                
            elif len(q)< ladders: heapq.heappush(q, diff)
                
            else: return max(j, 0)
            
                
        return n-1