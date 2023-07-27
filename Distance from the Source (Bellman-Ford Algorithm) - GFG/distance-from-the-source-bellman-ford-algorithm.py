#User function Template for python3

class Solution:
    # Function to construct and return cost of MST for a graph
    # represented using adjacency matrix representation
    '''
    V: nodes in graph
    edges: adjacency list for the graph
    S: Source
    '''
    def bellman_ford(self, V, edges, S):
        #code here
        dist = [int(1e8)]*V
        dist[S] = 0
        for i in range(V):
            for i in edges:
                source = i[0]
                dest = i[1]
                weight = i[2]
                if dist[source] != int(1e8) and dist[source] + weight < dist[dest]:
                    dist[dest] = dist[source]+weight
        
        for i in edges:
            source = i[0]
            dest = i[1]
            weight = i[2]
            if dist[source] != int(1e8) and dist[source] + weight < dist[dest]:
                return [-1]
        
        return dist
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
        edges = []
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            edges.append([u,v,w])
        S=int(input())
        ob = Solution()
        
        res = ob.bellman_ford(V,edges,S)
        for i in res:
            print(i,end=" ")
        print()
# } Driver Code Ends