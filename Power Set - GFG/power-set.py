#User function Template for python3

class Solution:
	def AllPossibleStrings(self, s):
		# Code here
		def add(i,arr):
		    r = ""
		    for k in arr:
		        r += k
		    if r != "":
		        res.append(r)
		    for a in range(i,len(s)):
		        arr.append(s[a])
		        add(a+1,arr)
		        arr.pop()
		    return 
		res = []
		add(0,arr= [])
		res.sort()
		return res
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()
		ob = Solution();
		ans = ob.AllPossibleStrings(s)
		for i in ans:
			print(i, end = " ");
		print()
# } Driver Code Ends