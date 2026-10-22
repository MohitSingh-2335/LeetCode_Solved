class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1]*len(nums)
        n=1
        m=1
        for i in range(len(nums)):
            ans[i] = n
            n *= nums[i]
        for i in range(len(nums)-1,-1,-1):
            ans[i] *= m
            m *= nums[i]
        return ans