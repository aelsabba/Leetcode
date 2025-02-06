# class Number:
#     def __init__(self,value,index):
#         self.index = index
#         self.value = value
# # class Solution:
# #     def twoSum(self, nums: List[int], target: int) -> List[int]:
# #         if (not nums or
# #             len(nums) < 2):
# #             return None
# #         Arr = [None] * len(nums)
# #         for i in range(len(nums)):
# #             Arr[i] = Number(nums[i],i)
# #         sortedArr = sorted(Arr,key= lambda Num : Num.value)
# #         leftPointer = 0
# #         rightPointer = len(sortedArr) - 1
# #         while leftPointer < rightPointer:
# #             if sortedArr[leftPointer].value + sortedArr[rightPointer].value == target:
# #                 return [sortedArr[leftPointer].index,sortedArr[rightPointer].index]
# #             elif sortedArr[leftPointer].value + sortedArr[rightPointer].value > target:
# #                 rightPointer -= 1
# #             else:
# #                 leftPointer += 1
# #         return None
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsDict = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if nums[i] in numsDict:
                return [i,numsDict[nums[i]]]
            else:
                numsDict[diff] = i
        return []