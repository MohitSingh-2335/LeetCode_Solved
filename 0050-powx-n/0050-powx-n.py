class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        num = abs(n)
        if n % 2 == 0:
            ans = self.myPow(x, num/2)
            ans = ans * ans
        else:
            ans = x * self.myPow(x, num - 1)
        
        if n < 0:
            return (1/ans)
        return ans
        