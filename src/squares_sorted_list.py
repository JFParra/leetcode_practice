# https://leetcode.com/problems/squares-of-a-sorted-array/description/
# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in
# non-decreasing order.


def sorted_squares(nums: list[int]) -> list[int]:
    final = []
    # trivial approach O(nlogn) but this solution is faster than 2 pointer below ??
    # for i in nums:
    #     final.append(i*i)
    # final.sort()

    # two pointer solution
    left = 0
    right = len(nums) - 1

    while left <= right:
        temp = []

        # left side bigger
        if abs(nums[left]) > abs(nums[right]):
            temp.append(nums[left] * nums[left])
            left += 1
        # right side bigger
        elif abs(nums[left]) < abs(nums[right]):
            temp.append(nums[right] * nums[right])
            right -= 1

        # left = right
        else:
            temp.append(nums[left] * nums[right])
            left += 1

        final = temp + final

    return final


if __name__ == "__main__":
    # Input: s = "abc", t = "ahbgdc"
    print(sorted_squares([-4, -1, 0, 3, 10]))
