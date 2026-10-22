class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=2
        for j in range(2, len(nums)):
            if k < 2 or nums[j] != nums[k-2]:
                nums[k]=nums[j]
                k+=1
        return k
            
            

