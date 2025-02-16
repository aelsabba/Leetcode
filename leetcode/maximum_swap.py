class Solution(object):
    def swap(self, arr, left, right):
        temp = arr[left]
        arr[left] = arr[right]
        arr[right] = temp
        return None

    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        arr = [int(digit) for digit in str(num)]
        left_idx = len(arr) - 1
        max_idx = len(arr) - 1
        max_val = arr[max_idx]
        right_idx = -1
        i = len(arr) - 1
        while i >= 0:
            if (arr[i] > max_val):
                max_val = arr[i]
                max_idx = i
                continue

            if (arr[i] < max_val):
                left_idx = i
                right_idx = max_idx

            i -= 1

        if right_idx:
            self.swap(arr, left_idx, right_idx)

        rtrn = int("".join([str(d) for d in arr]))

        return rtrn
