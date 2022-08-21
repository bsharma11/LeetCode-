class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        lst = [nums[0]]
        ans = 0
        for i in range(1,len(nums)):
            idx = bisect_right(lst,nums[i]*2)
            ans+=len(lst)-idx
            lst.insert(bisect_right(lst,nums[i]),nums[i])
        return ans
        
            