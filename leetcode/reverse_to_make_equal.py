
# Reverse to Make Equal
# Given two arrays A and B of length N, determine if there is a way to make A equal to B by reversing any subarrays from array B any number of times.
# Signature
# bool areTheyEqual(int[] arr_a, int[] arr_b)
# Input
# All integers in array are in the range [0, 1,000,000,000].
# Output
# Return true if B can be made equal to A, return false otherwise.
# Example
# A = [1, 2, 3, 4]
# B = [1, 4, 3, 2]
# output = true
# After reversing the subarray of B from indices 1 to 3, array B will equal array A.

import math


# Add any extra import statements you may need here


# Add any helper functions you may need here

def check_reverse(array_a: list, array_b: list, left: int):
    right = len(array_a) - 1
    while left < right:
        if array_a[left] == array_b[right]:
            subArrayLength = 1
            while (subArrayLength <= right - left + 1):
                if array_a[left
                           + subArrayLength - 1] == array_a[right - subArrayLength - 1]:
                    subArrayLength += 1
                else:
                    break
            if (left + subArrayLength == right):
                return (left, right)
            right -= 1
        else:
            right -= 1
    return (left, right)


def are_they_equal(array_a, array_b):
    # Write your code here
    if len(array_a) != len(array_b):
        return False

    left = 0
    while left < len(array_a):
        if array_a[left] == array_b[left]:
            left += 1
        else:
            (left, right) = check_reverse(array_a, array_b, left)
            if left == right:
                return False
            else:
                left += (right - left) + 1
    return True


# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.
def printString(string):
    print('[\"', string, '\"]', sep='', end='')


test_case_number = 1


def check(expected, output):
    global test_case_number
    result = False
    if expected == output:
        result = True
    rightTick = '\u2713'
    wrongTick = '\u2717'
    if result:
        print(rightTick, 'Test #', test_case_number, sep='')
    else:
        print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
        printString(expected)
        print(' Your output: ', end='')
        printString(output)
        print()
    test_case_number += 1


if __name__ == "__main__":
    n_1 = 4
    a_1 = [1, 2, 3, 4, 5, 6, 7]
    b_1 = [1, 4, 3, 2, 5, 6, 7]
    expected_1 = True
    output_1 = are_they_equal(a_1, b_1)
    check(expected_1, output_1)

    n_2 = 4
    a_2 = [1, 2, 3, 4]
    b_2 = [1, 2, 3, 5]
    expected_2 = False
    output_2 = are_they_equal(a_2, b_2)
    check(expected_2, output_2)

    # Add your own test cases here
