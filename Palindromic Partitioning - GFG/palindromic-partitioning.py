#User function Template for python3

class Solution:
    def palindromicPartition(self, string):
        
        def isPalindrome(i,j):
            while i <j:
                if string[i] != string[j]:
                    return False
                i +=1
                j -=1 
            return True
        
        def check(i):
            if i == len(string):
                return 0
            if i in dp:
                return dp[i]
            mn = int(1e9)
            for j in range(i,len(string)):
                if isPalindrome(i,j):
                    cost = 1+ check(j+1)
                    mn = min(cost,mn)
                dp[i] = mn
            return dp[i]
            
        dp = {}
        return check(0) -1




#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        string = input()
        
        ob = Solution()
        print(ob.palindromicPartition(string))
# } Driver Code Ends