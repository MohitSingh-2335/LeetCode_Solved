class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        set_nums = set(nums)
        longest = []
        streak = 0
        if not set_nums:
            return 0
        if len(set_nums) == 1:
            return 1
        for ele in set_nums:
            if ele - 1 not in set_nums:
                streak = 1
                nele = ele
                while nele + 1 in set_nums:
                    streak += 1
                    nele += 1
                longest.append(streak)

        return max(longest) 