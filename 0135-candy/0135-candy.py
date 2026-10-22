class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candy = [1]*n
        for i in range(n):
            if i-1 >= 0 and ratings[i] > ratings[i-1]:
                candy[i] = candy[i-1] + 1
        for i in range(n-1,-1,-1):
            if i+1 < n and ratings[i] > ratings[i+1]:
                candy[i] = max(candy[i], candy[i+1] + 1)    
        return sum(candy)