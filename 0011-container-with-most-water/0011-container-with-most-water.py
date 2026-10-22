class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        count = 0
        i = 0 
        j = -1

        while (i < len(height) and j >= -len(height)):

            mini = min(height[i], height[j])

            res = mini * (len(height) + j - i)

            if res >= count:

                count = res

            if height[i] > height[j]:
                
                j -= 1

            else:

                i += 1

        return count