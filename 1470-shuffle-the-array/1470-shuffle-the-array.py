class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        a = nums[n:]
        del nums[n:]
        for i in range(len(a)):
            if i == 0:
                nums[i + 1:i + 1] = [a[i]]
            else:
                nums[i + i + 1:i + i + 1] = [a[i]]
        return nums