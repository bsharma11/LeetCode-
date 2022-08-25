class Solution:
    def minDeletions(self, s: str) -> int:
        d = {}
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
           
        a = [-cnt for char,cnt in d.items()]
        a.sort()
        count = 0
        # print(a)
        for i in range(1,len(a)):
            if a[i] == a[i-1]:
                a[i] += 1
                count += 1
                continue
            if a[i] < a[i-1]:
                
                if a[i-1] == 0:
                    while a[i] != 0:
                        count+= 1
                        a[i] += 1
                else:
                    while a[i] -1 != a[i-1]:
                        count += 1
                        a[i] += 1
                    continue
            else:
                continue
        # print(count)
        return count  
                