import math


class Solution:

    def __init__(self, w: List[int]):
        self.cum_sum = []
        cum_sum = 0
        for weight in w:
            cum_sum += weight
            self.cum_sum.append(cum_sum)
        self.total_sum = cum_sum

    def binary_search(self, value):
        left = 0
        right = len(self.cum_sum) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if (value < self.cum_sum[mid] and
                    value > self.cum_sum[mid - 1]):
                return mid
            elif value > self.cum_sum[mid]:
                left = mid + 1
            else:
                right = mid - 1

        return mid

    def pickIndex(self) -> int:
        random_num = self.total_sum * random.random()
        return self.binary_search(random_num)

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()