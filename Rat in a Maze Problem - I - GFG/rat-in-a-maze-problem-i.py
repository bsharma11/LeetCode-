#User function Template for python3

class Solution:
    def findPath(self, m, n):
        # code here
        if m[0][0] == 0 or m[n-1][n-1] == 0:
            return [-1]
        def check(i,j,s):
            if i == n-1 and j == n-1:
                res.append("".join(s))
                return 
            
            for a in directions:
                x = a[0] +i
                y = a[1] + j
                d = a[2]
                if x <0  or y < 0 or x >= n or y >= n or m[x][y] != 1 or (x,y) in vis:
                    continue
                else:
                    s.append(d)
                    vis.add((x,y))
                    check(x,y,s)
                    vis.remove((x,y))
                    s.pop()
            return 
        res = []
        vis = set()
        vis.add((0,0))
        directions = [[0,1,"R"],[1,0,"D"],[-1,0,"U"],[0,-1,"L"]]
        check(0,0,[])
        res.sort()
        return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        
        matrix = [[0 for i in range(n[0])]for j in range(n[0])]
        k=0
        for i in range(n[0]):
            for j in range(n[0]):
                matrix[i][j] = arr[k]
                k+=1
        ob = Solution()
        result = ob.findPath(matrix, n[0])
        result.sort()
        if len(result) == 0 :
            print(-1)
        else:
            for x in result:
                print(x,end = " ")
            print()
# } Driver Code Ends