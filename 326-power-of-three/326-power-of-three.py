class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 0:
            return False
        if n ==1 :
            return True
        while n != 0:
            x = n//3
            if x == 1 and n %3 ==0:
                return True
            if x % 3 == 0 and n%3 != 0:
                return False
            if x %3 != 0:
                return False
            n = n//3
        return True