class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        a = []
        i = 0
        hash_list = [-1] * 127
        for j, char in enumerate(s):
            ind = ord(char)
            if hash_list[ind] >= i:
                i = hash_list[ind] + 1
            hash_list[ind] = j

            count = j - i + 1
            a.append(count)
        return max(a) if a else 0
                