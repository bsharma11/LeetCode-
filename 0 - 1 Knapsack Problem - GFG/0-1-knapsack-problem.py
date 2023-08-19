#User function Template for python3

class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
        def check(i,w):
            if i >= len(wt) or wt == 0:
                return 0
            if (i,w) in dp:
                return dp[(i,w)]
            if wt[i] <= w:
                dp[(i,w)] = max(val[i] + check(i+1,w-wt[i]),check(i+1,w))
            else:
                dp[(i,w)] = check(i+1,w)
            return dp[(i,w)]
        # code here
        dp = {}
        val,wt = zip(*sorted(zip(val,wt),reverse = True))
        # print(val,wt)
        return check(0,W)        


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        W = int(input())
        val = list(map(int,input().strip().split()))
        wt = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.knapSack(W,wt,val,n))
# } Driver Code Ends