class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq_dic = {}
        for element in nums:
            if element not in freq_dic:
                freq_dic[element] = 1
            else:
                freq_dic[element] += 1
        sorted_dic = dict(sorted(freq_dic.items(), key = lambda ele : -ele[1]))

        return list(sorted_dic.keys())[:k]