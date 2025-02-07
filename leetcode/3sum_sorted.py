class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []

        def three_sum_helper(i):
            low = i + 1
            hi = len(nums) - 1
            while low < hi:
                total = nums[i] + nums[low] + nums[hi]
                if total < 0:
                    low = low + 1

                if total > 0:
                    hi = hi - 1

                if total == 0:
                    results.append([nums[i],nums[low],nums[hi]])
                    low += 1
                    hi -= 1
                    while low < hi and nums[low] == nums[low -1]:
                        low += 1

        nums.sort()

        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i - 1] != nums[i]:
                three_sum_helper(i)

        return results
