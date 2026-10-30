class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result = []
        def fun(i, sbnum):
            if i == len(nums):
                result.append(sbnum.copy())
                return
            sbnum.append(nums[i])
            fun(i + 1, sbnum)
            sbnum.pop()
            fun(i + 1, sbnum)
        fun(0, [])
        return result