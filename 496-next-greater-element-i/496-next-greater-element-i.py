class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dc = {}
        a = []
        x = 0
        for i in nums2:
            dc[i] = x
            x += 1
        for i in nums1:
            val = dc[i]
            for j in range(val+1,len(nums2)):
                if nums2[j] > i:
                    a.append(nums2[j])
                    break
            else:
                a.append(-1)
        return a
                