class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        a = []
        for i in range(0, len(nums) - k+1):
            win = nums[i:k+i]
            count = Counter(win)
            sorteditem = sorted(count.items(), key = lambda p : (p[1],p[0]), reverse=True)
            top = sorteditem[:x]
            b = sum(a * freq for a, freq in top)
            a.append(b)
        return a