class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        if len(strs) == 0:
            return strs
        sorted_dic = {}
        for element in strs:
            value = "".join(sorted(element))
            if value not in sorted_dic:
                sorted_dic[value] = []
            sorted_dic[value].append(element) 
        return list(sorted_dic.values())
            
