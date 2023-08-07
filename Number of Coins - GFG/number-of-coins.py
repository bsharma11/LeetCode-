#User function Template for python3
import math
class Solution:
        
    def minCoins(self, coins, M, V):
        n =len(coins)
        dp = [[-1]*(V+1) for i in range(n+1)]
        def helper(i,t) :
            if i<=0 : return math.inf
            if t <= 0: return 0 
            # print(i,t,len(dp),len(dp[0]))
            if dp[i][t] != -1 : 
                return dp[i][t]
            if coins[i-1]<= t : 
                dp[i][t] = min(1+helper(i,t-coins[i-1],),helper(i-1,t))
            else:
                dp[i][t] = helper(i-1,t)
            return dp[i][t]

        x = helper(n,V)
        if x!=math.inf : 
            return x
        return -1 

        
        # code here

    






#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		v,m = input().split()
		v,m = int(v), int(m)
		coins = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.minCoins(coins,m,v)
		print(ans)

# } Driver Code Ends