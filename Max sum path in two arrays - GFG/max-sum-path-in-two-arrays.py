#Your task is to complete this function
#Function should return an integer denoting the required answer
class Solution:
    def maxSumPath(self, arr1, arr2, m, n):
        i = j = 0
        result = 0
        sumA = 0
        sumB = 0

        while i < m and j < n:
            if arr1[i] < arr2[j]:
                sumA += arr1[i]
                i += 1
            elif arr1[i] > arr2[j]:
                sumB += arr2[j]
                j += 1
            else:  # Common element found
                result += max(sumA, sumB) + arr1[i]
                sumA = 0
                sumB = 0
                i += 1
                j += 1
        
        while i < m:
            sumA += arr1[i]
            i += 1

        while j < n:
            sumB += arr2[j]
            j += 1

        result += max(sumA, sumB)

        return result
#{ 
 # Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        m,n = list(map(int, input().strip().split()))
        arr1 = list(map(int, input().strip().split()))
        arr2 = list(map(int, input().strip().split()))
        print(Solution().maxSumPath(arr1, arr2, m, n))
# Contributed by: Harshit Sidhwa
# } Driver Code Ends