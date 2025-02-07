class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        stack = [(len(heights) - 1, heights[-1])]
        i = len(heights) - 2
        while i >= 0:
            if heights[i] > stack[-1][1]:
                stack.append((i, heights[i]))

            i -= 1
        return [(lambda x : x[0]) (x) for x in stack[::-1]]