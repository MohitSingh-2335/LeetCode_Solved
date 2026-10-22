class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        end = 0
        highLen = 0
        max_count = 0
        strS = list(s)
        freq = {}

        if len(s) < 0:
            return 0

        while (end < len(strS)):
            end_char = strS[end]
            freq[end_char] = freq.get(end_char, 0) + 1
            
            if freq[end_char] > max_count:
                max_count = freq[end_char]
                
            if (end - start + 1) - max_count > k:
                start_char = strS[start]
                freq[start_char] -= 1
                start += 1
                
            currentLen = end - start + 1
            if currentLen > highLen:
                highLen = currentLen
                
            end += 1

        return highLen
