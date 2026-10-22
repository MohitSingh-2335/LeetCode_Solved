class Solution:
    def isPalindrome(self, s: str) -> bool:
        c=r'[^a-zA-Z0-9]'
        s1=re.sub(c,"",s).lower()
        a=0
        b=len(s1)-1
        while a < b:
            if s1[a]==s1[b]:
                a+=1
                b-=1
            else:
                return False
        return True
