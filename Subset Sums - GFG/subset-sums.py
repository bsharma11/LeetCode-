#User function Template for python3
class Solution:
	def subsetSums(self, arr, N):
		# code here
        res = [0]
        
        
        def calc(idx,a):
            org= a
            if idx == len(arr):
                return 
            a += arr[idx]
            res.append(a)
            
            calc(idx+1,org)
            calc(idx+1,a)
        
        calc(0,0)
        res.sort()
        return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        N = int(input())
        arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.subsetSums(arr, N)
        ans.sort()
        for x in ans:
            print(x,end=" ")
        print("")

# } Driver Code Ends