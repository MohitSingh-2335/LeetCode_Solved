class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i, tar in enumerate(nums):
            if tar==target:
                return i
            elif tar > target:
                return i
        return len(nums)


