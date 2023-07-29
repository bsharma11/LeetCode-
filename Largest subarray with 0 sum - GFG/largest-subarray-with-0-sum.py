#Your task is to complete this function
#Your should return the required output
class Solution:
    def maxLen(self, n, arr):
        #Code here
        mpp = {}
        maxi = 0
        sum = 0
        for i in range(n):
            sum += arr[i]
            if sum == 0:
                maxi = i + 1
            else:
                if sum in mpp:
                    maxi = max(maxi, i - mpp[sum])
                else:
                    mpp[sum] = i
        return maxi


#{ 
 # Driver Code Starts
if __name__=='__main__':
    t= int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maxLen(n ,arr))
# Contributed by: Harshit Sidhwa
# } Driver Code Ends