#User function Template for python3

class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,n,arr,dep):
        
        # code here
        
        arr.sort()
        dep.sort()
        platforms = 1  # minimum number of platforms needed
        max_platforms = 1  # maximum number of platforms needed
        
        i = 1  # pointer for arrival array
        j = 0  # pointer for departure array
    
        while i < n and j < n:
            if arr[i] <= dep[j]:
                platforms += 1
                i += 1
                max_platforms = max(max_platforms, platforms)
            else:
                platforms -= 1
                j += 1

        return max_platforms
        # print(dep,arr)
#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        arrival = list(map(int, input().strip().split()))
        departure = list(map(int, input().strip().split()))
        ob=Solution()
        print(ob.minimumPlatform(n,arrival,departure))
# } Driver Code Ends