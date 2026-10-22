class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        max_value = float('-inf')
        res = 0

        for i in nums:
            if res < 0:
                res = 0
            res += i

            if res > max_value:
                max_value = res

        return max_value
             