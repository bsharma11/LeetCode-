class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == k:
            return "0"
        arr = []
        i = 0 
        count = 0
        while i <len(num):
            if count == k:
                arr.append(num[i])
                i+= 1
                continue
            if arr == []:
                arr.append(num[i])
                i += 1
                continue
            if int(num[i]) < int(arr[-1]):
                while arr != [] and int(arr[-1]) > int(num[i]):
                    if count == k:
                        break
                    arr.pop()
                    count += 1
                arr.append(num[i])
                i+=1
                continue
            arr.append(num[i])
            i += 1
        if k != count:
            while k != count:
                arr.pop()
                count += 1
        s = ""
        for i in arr:
            s+= i
        x = int(s)
        return str(x)
            
                    