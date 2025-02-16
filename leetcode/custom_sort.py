# Input: order = "bcafg", s = "abcd"

# Output: "bcad"

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        def get_order(char):
            if char in order_dict:
                return order_dict[char]
            else:
                return 27

        order_dict = {order[i] : i for i in range(len(order))}
        return "".join(sorted(s ,key = lambda char : get_order(char)))