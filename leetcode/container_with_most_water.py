class Solution:
    def calculate_volume(self, height, i, j):
        volume = min(height[i], height[j]) * (j - i)
        return volume

    def maxArea(self, height: List[int]) -> int:
        volumeMax = 0
        i = 0
        j = len(height) - 1
        while (j > i):
            volume = self.calculate_volume(height, i, j)
            if volume > volumeMax:
                volumeMax = volume
            if height[j] > height[i]:
                i += 1
            else:
                j -= 1
        return volumeMax


