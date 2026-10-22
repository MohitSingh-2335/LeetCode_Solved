class Solution:
    def check(self, nums: List[int]) -> bool:
        a = sorted(nums)
        i = 0
        while (i < len(nums)):
            b = a.pop(0)
            a.append(b)
            if a == nums:
                return True
                break
            i += 1
        else:
            return False