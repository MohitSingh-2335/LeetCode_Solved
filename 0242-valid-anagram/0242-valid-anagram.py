class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = [0]*26
        for char in s:
            index = ord(char) - ord('a')
            count[index] += 1 
        for char in t:
            index2 = ord(char) - ord('a')
            count[index2] -= 1
        if count == [0]*26:
            return True
        else:
            return False