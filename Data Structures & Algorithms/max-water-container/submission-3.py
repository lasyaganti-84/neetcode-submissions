class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxarea = 0

        i = 0
        j = len(heights) - 1
        maxrea = 0

        while i < j:
            curr_area = (j - i) * min(heights[i], heights[j])
            maxarea = max(curr_area, maxarea)

            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1

        return maxarea




        # for i in range(len(heights)):
        #     for j in range(i + 1, len(heights)):
        #         area = (j - i) * min(heights[i], heights[j])
        #         maxarea = max(maxarea, area)
                
        # return maxarea