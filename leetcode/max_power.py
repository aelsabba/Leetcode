class Solution:
    def maxPower(self, s: str) -> int:
        longest = 1
        left_pointer = 0
        right_pointer = 1
        while right_pointer < len(s):
            if s[right_pointer] != s[left_pointer]:
                left_pointer = right_pointer  # left = 1
            if right_pointer - left_pointer + 1 > longest:
                longest = right_pointer - left_pointer + 1  # longest = 1, longest = 2
            right_pointer += 1  # right = 2

        return longest