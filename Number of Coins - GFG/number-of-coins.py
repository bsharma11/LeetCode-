#User function Template for python3
class Solution:
	def minCoins(self, coins, M, V):
		# code here
        def check(target,i):
            if target == 0:
                return 0
            if i >= len(coins):
                return int(1e9)
            if (target,i) in dp:
                return dp[(target,i)]
            if coins[i] <= target:
                dp[(target,i)] = min(1+check(target-coins[i],i),check(target,i+1))
            else:
                dp[(target,i)] = check(target,i+1)
            return dp[(target,i)]
        dp = {}
        coins.sort(reverse = True)
        x = check(V,0)
        if  x >= int(1e9):
            return -1
        return x
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

# } Driver