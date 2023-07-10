#User function Template for python3

class Solution:
    def findPath(self, m, n):
        # code here
        
        def travel(i,j,vis,ans):
            if i == n-1 and j== n-1:
                self.res.append(ans)
                return
            if i +1<n and m[i+1][j] == 1 and (i+1,j) not in vis:
                vis.append((i,j))
                travel(i+1,j,vis,ans+"D")
                vis.pop()
            if j -1 >= 0 and m[i][j-1] == 1 and (i,j-1) not in vis:
                vis.append((i,j))
                travel(i,j-1,vis,ans+'L')
                vis.pop()
            if j +1 < n and m[i][j+1] == 1 and (i,j+1) not in vis:
                vis.append((i,j))
                travel(i,j+1,vis,ans+'R')
                vis.pop()
            if i -1 >= 0 and m[i-1][j] == 1 and (i-1,j) not in vis:
                vis.append((i,j))
                travel(i-1,j,vis,ans+"U")
                vis.pop()
        self.res = []
        if m[0][0] == 0 or m[n-1][n-1] == 0:
             return self.res
        travel(0,0,[],"")
        # if not self.res:
        #     return -1
        # else:
        return self.res


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