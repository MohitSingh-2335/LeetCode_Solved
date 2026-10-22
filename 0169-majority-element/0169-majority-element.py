class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        a=None
        b=0
        for num in nums:
            if b==0:
                a=num
                b=1
            elif num==a:
                b+=1
            else:
                b-=1
        return a

            