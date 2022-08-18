class Solution:
    def reorganizeString(self, s: str) -> str:
        dc = {}
        for i in s:
            if i in dc:
                dc[i] += 1
            else:
                dc[i] = 1
        maxHeap = [[-cnt, char] for char, cnt in dc.items()]
        heapq.heapify(maxHeap) # O(n)
        print(maxHeap)
        prev = None
        res = ""
        
        while maxHeap or prev:
            if prev and not maxHeap:
                return ""
            
            cnt, char = heapq.heappop(maxHeap)
            res += char
            cnt +=1 # its a min heap so we add, since the vals are negative, actually we want to subtract
            
            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None
            if cnt !=0:
                prev = [cnt, char]
                
        return res
                