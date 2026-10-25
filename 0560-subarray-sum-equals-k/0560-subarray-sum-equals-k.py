class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        output = 0
        prefix_dic = {0:1}
        sum_ele = 0
        for ele in nums:
            sum_ele += ele
            if prefix_dic.get(sum_ele - k, 0):
                output += prefix_dic.get(sum_ele - k, 0)
            prefix_dic[sum_ele] = prefix_dic.get(sum_ele, 0) + 1 
        return output