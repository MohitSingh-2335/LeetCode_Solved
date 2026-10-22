class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        q = n
        while q > 1:
            if q % 3 != 0:
                return False
                break
            q = q // 3
        else:
            if q == 1:
                return True
            else:
                return False