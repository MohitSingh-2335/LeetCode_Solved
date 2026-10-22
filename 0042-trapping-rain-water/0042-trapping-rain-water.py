class Solution:
    def trap(self, height: List[int]) -> int:
        count = []
        water = 0
        emp1 = [0]*len(height)
        emp2 = [0]*len(height)
        runlmax = 0
        runrmax = 0
        for i in range(len(height)):
            if runlmax < height[i]:
                runlmax = height[i]
            emp1[i] = runlmax
        for j in range(len(height)-1,-1,-1):
            if runrmax < height[j]:
                runrmax = height[j]
            emp2[j] = runrmax
        for k in range(len(height)):
            water = min(emp1[k] , emp2[k]) - height[k]
            if water < 0:
                water = 0
            count.append(water)
        return sum(count)