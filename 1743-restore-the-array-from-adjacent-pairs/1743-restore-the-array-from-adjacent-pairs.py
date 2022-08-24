class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
#         if len(adjacentPairs) == 1:
#             return [adjacentPairs[0][0],adjacentPairs[0][1]]
#         a = [None]*(len(adjacentPairs)+1)
#         dc = {}
#         for i in range(len(adjacentPairs)):
#             if adjacentPairs[i][0] in dc:
#                 dc[adjacentPairs[i][0]] += 1
#             if adjacentPairs[i][0] not in dc:
               
#                 dc[adjacentPairs[i][0]] = 1
#             if adjacentPairs[i][1] in dc:
               
#                 dc[adjacentPairs[i][1]] += 1
#             if adjacentPairs[i][1] not in dc:
#                 dc[adjacentPairs[i][1]] = 1
#         b = [[num,cnt] for num,cnt in dc.items()]
#         i = 0 
#         print(b)
#         while i < len(b):
#             print(i)
#             if b[i][1] == 2:
#                 if i % 2 == 0: 
#                     a[i+1] = b[i][0]
#                     a[i] = b[i+1][0]
#                     i += 2
#                     continue
#                 else:
#                     a[i] = b[i][0]
#                     i += 1
#                     continue
#             if b[i][1] == 1:
#                 a[i] = b[i][0]
#                 i+= 1
#                 continue
#         print(a)
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
        
        