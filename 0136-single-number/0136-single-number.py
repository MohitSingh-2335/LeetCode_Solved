class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        dic = {}

        for i in nums:

            if i in dic:

                dic[i] += 1

            else:

                dic[i] = 1
        
        a = [j for j, k in dic.items() if k == 1]

        return (a[0])