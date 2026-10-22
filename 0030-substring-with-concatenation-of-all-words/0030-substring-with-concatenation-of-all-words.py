class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        
        from collections import Counter

        final = []
        element = len(words[0])
        lenght = len(words)
        temp1_list = Counter(words)

        for first in range(len(s)):
            b = s[first : first + (element * lenght)]
            a = []
            for last in range(0, len(b), element):
                c = b[last : last + element]
                a.append(c)
            temp2_list = Counter(a)
            if temp1_list == temp2_list:
                final.append(first)

        return final

        return final