import heapq
from collections import *
class Solution:

    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V, adj, S):
        q=deque()
        q.append([S,0])
        distance=[float('inf')]*V
        distance[S]=0
        while q:
            node,dis=q.popleft()
            for child in adj[node]:
                if dis+child[1]<distance[child[0]]:
                    distance[child[0]]=dis+child[1]
                    q.append([child[0],dis+child[1]])
        return distance
        # from collections import *
        # q=deque()
        # distance=[float('inf')]*V
        # distance[S]=0
        # q.append([S,0])
        # while q:
        #     node,dis=q.popleft()
        #     for child in adj[node]:
        #         if child[1]+dis<distance[child[0]]:
        #             distance[child[0]]=dis+child[1]
        #             q.append([child[0],distance[child[0]]])
        # return distance
        





#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        S=int(input())
        ob = Solution()
        
        res = ob.dijkstra(V,adj,S)
        for i in res:
            print(i,end=" ")
        print()
# } Driver Code Ends