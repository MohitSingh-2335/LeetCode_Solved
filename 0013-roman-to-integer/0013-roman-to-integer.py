class Solution:
    def romanToInt(self, s: str) -> int:
        l=0
        pv=0
        val={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        for i in range(len(s)-1,-1,-1):
            cv=val[s[i]]
            if cv < pv:
                l-=cv
            else:
                l+=cv
            pv=cv
        return l    
