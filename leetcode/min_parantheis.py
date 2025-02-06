class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        l = 0
        r = 0
        added = 0

        for char in s:
            if char == "(":
                l += 1
            else:
                if r < l:
                    r += 1
                else:
                    added += 1

        return added + l - r