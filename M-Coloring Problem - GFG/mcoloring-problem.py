#User function Template for python3


#Function to determine if graph can be coloured with at most M colours such
#that no two adjacent vertices of graph are coloured with same colour.
def graphColoring(graph, k, V):
    color = [-1]*V
    def isPossible(node,i,color):
        for _ in range(V):
            if graph[node][_]==1: #this check wether an edge exists between the two nodes
                if color[_] == i:
                    return False
        return True
    def coloring(node,color):
        if node == V:
            return True 
        res=False
        for i in range(k):
            if isPossible(node,i,color):
                color[node] = i 
                res=res or coloring(node+1,color)
                color[node] = -1 
        return res
    if coloring(0,color):
        return 1 
    return 0
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # pos_cols=[]
    # for i in range(k):
    #     pos_cols.append(i)
    # def rec(node,d):
    #     if node==V:
    #         return True
    #     p=pos_cols.copy()
    #     for i in range(V):
    #         if graph[node][i]==1:
    #             if i in d:
    #                 if d[i] in p:
    #                     p.remove(d[i])
    #     if len(p)==0:
    #         return False
            
    #     x=False
    #     for i in p:
    #         d[node]=i
    #         x=x or rec(node+1,d)
    #         del d[node]
    #     return x
        
    # return rec(0,{})
    
    





#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while(t>0):
        V = int(input())
        k = int(input())
        m = int(input())
        list = [int(x) for x in input().strip().split()]
        graph = [[0 for i in range(V)] for j in range(V)]
        cnt = 0
        for i in range(m):
            graph[list[cnt]-1][list[cnt+1]-1]=1
            graph[list[cnt+1]-1][list[cnt]-1]=1
            cnt+=2
        if(graphColoring(graph, k, V)==True):
            print(1)
        else:
            print(0)

        t = t-1

# } Driver Code Ends