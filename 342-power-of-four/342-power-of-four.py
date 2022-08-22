class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1:
            return True
        if n == 0:
            return False
        while n != 0:
            x = n//4
            if x == 1 and n%4 ==0:
                return True
            if x % 4 != 0 or n % 4 != 0 :
                return False
            n = n//4
        return True
        