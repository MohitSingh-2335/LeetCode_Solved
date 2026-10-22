class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        stri=""
        for i in range(len(strs[0])):
            char1=strs[0][i]
            for j in range(len(strs)):
                if i>=len(strs[j]) or strs[j][i]!=char1:
                  return stri
            stri +=char1
        return stri