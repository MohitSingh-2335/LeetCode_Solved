class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        count = []

        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            while (j < k):
                total_sum = nums[i] + nums[j] + nums[k]

                if total_sum < 0:
                    j += 1
                elif total_sum > 0:
                    k -= 1
                else:
                    count.append([nums[i],nums[j],nums[k]])
                    j += 1
                    k -= 1

                    while nums[j] == nums[j - 1] and j < k:
                        j += 1

        return count
                    