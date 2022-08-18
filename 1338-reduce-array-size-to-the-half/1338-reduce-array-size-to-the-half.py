class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        x = len(arr)
        dt = {}
        for i in arr:
            if i in dt:
                dt[i] +=1
            else:
                dt[i] = 1
        a = []
        for i in dt:
            a.append([i,dt[i]])
        a.sort(key = lambda x: x[1])
        i = len(a) -1
        count = 0
        s = 0
        while i >= 0:
            if a[i][1] >= x//2:
                return 1
            s += a[i][1]
            count += 1
            if s >= x//2:
                return count
            i -= 1
            