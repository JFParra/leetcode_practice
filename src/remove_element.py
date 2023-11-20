# https://leetcode.com/problems/remove-element/description/
# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the
# elements may be changed. Then return the number of elements in nums which are not equal to val.
# Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the
# following things:

# - Change the array nums such that the first k elements of nums contain the elements which are not equal to val.
#   The remaining elements of nums are not important as well as the size of nums.
# - Return k.


def remove_element(nums: list[int], val: int) -> int:
    removed_count = 0

    for i, v in enumerate(nums):
        if v != val:
            nums[removed_count] = nums[i]
            removed_count += 1

    return removed_count


if __name__ == "__main__":
    # Input: s = "abc", t = "ahbgdc"
    print(remove_element([0, 1, 2, 2, 3, 0, 4, 2], 2))
