class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph=defaultdict(list)
        
        # creating the graph
        for u,v in adjacentPairs:
            graph[u].append(v)
            graph[v].append(u)
        cur=None
        # Find the key which have only one value. This means the key have only one adjacent element
        for u in graph:
            if len(graph[u])==1:
                cur=u
                break
        ans=[]
        vis=set()  
        
        while cur!=None:   # Traversing thorugh each node   
            ans.append(cur)
            vis.add(cur)
            adjacent=graph[cur]
            cur=None
            
            for x in adjacent:  # selecting the next adjacent element
                if x not in vis:
                    cur=x
        return ans
        
        