class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        res = sum(nums[0:k])
        tot = []
        tot.append(res/k)
        high = 0

        for i in range(k, len(nums)):

            res += nums[i] - nums[i - k]

            tot.append(res/k)

        high = max(tot)

        return high