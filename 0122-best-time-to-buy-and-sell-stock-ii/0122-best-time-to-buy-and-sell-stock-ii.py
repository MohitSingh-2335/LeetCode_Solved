class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mp=0
        p=0
        pv=prices[0]
        for i in prices[1:]:
            if i > pv:
                p=i-pv
                mp+=p
            pv=i
        return mp

            
