#User function Template for python3
from collections import deque
from typing import List
from queue import Queue
class Solution:
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        q=deque()
        q.append(0)
        isdone={}
        ans=[] 

        while q:
            cur=q.popleft()
            if cur not in isdone:
                isdone[cur]=1
                ans.append(cur)
            
            for i in adj[cur]:
                if i not in isdone:
                    q.append(i)
                    
        return  ans            
        # code here





#{ 
 # Driver Code Starts


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
		ob = Solution()
		ans = ob.bfsOfGraph(V, adj)
		for i in range(len(ans)):
		    print(ans[i], end = " ")
		print()
        

# } Driver Code Ends