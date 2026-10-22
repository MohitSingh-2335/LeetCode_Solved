class Solution:
    def reverseWords(self, s: str) -> str:
        a = s.strip()
        b = a.split()
        c = b[-1::-1]
        s = " ".join(c)
        return s